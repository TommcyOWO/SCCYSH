from fastapi import Depends, FastAPI,HTTPException,Request,Response
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import trio
from hypercorn.trio import serve
from hypercorn.config import Config

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from pymongo import MongoClient
from algoliasearch.search_client import SearchClient

#過濾器
from model import *

#oauth 初始化
from oauth import *

#初始化
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(redoc_url=None,docs_url=None)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#DB 初始化
#DB herf
client = MongoClient("mongodb://localhost:27017/")

#DB setup
count_db = client['count']
activity_db = client['activity']

users = count_db.users
id_users = count_db.id_users

ac_db = activity_db.databace

#阻擋request
@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=exc.status_code,
        content={"ERROR":f"Too many request,{exc.detail}"},
    )

#404 error handler
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"ERROR":exc.detail},
    )

#405 error handler
@app.exception_handler(405)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"ERROR":exc.detail},
    )

#main
#oauth path
@app.post("/register")
async def register_user(user: register_reset):
    users_db = users.find_one({"username":user.username})
    if users_db != None:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db = users.find_one({"email":user.email})
    if users_db != None:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_password = password_context.hash(user.password)
    users_db = {
        "email": user.email,
        "username": user.username,
        "password": hashed_password
    }
    users.insert_one(users_db)
    return {"message": "User registered successfully"}

@app.post("/logon")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    
    users_db = users.find_one({"username":username})
    verify_pas = password_context.verify(password,users_db["password"])
    if users_db == None or verify_pas == None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": password})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/reset")
async def reset_acount(user:register_reset):
    reset_acount_db = users.find_one({'username':user.username,'email':user.email})
    if reset_acount_db == None:
        raise HTTPException(status_code=400, detail="Username or Email not match.")

    h_password = password_context.hash(user.password)
    users.update_one({'name':user.username,'email':user.email},{'$set': {'password':h_password }})
    
    return {"message":"Reset done"}

if __name__ == "__main__":
    # config = Config()
    # config.bind = ["192.168.1.108:5000"]
    # trio.run(serve, app, config)
    
    uvicorn.run(app,host="0.0.0.0",port=5000)
    # uvicorn.run(app,host='0.0.0.0',ssl_keyfile='./key.pem',ssl_certfile='./cert.pem')