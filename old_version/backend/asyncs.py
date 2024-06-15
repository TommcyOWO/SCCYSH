from pymongo import MongoClient
from algoliasearch.search_client import SearchClient

#DB 初始化
#DB herf
client = MongoClient("mongodb://localhost:27017/")

#DB setup
count_db = client['count']
activity_db = client['activity']

#登入部分
users = count_db.users

#algoli 同步
temporary = activity_db.temporary
formal = activity_db.formal

# 連接 Algolia
Algolia_client = SearchClient.create('K6A25QQ0RF', '088f30d58ab7456ac5570b8b93b634ca')
index = Algolia_client.init_index('CSG')

async def async_data():
    try:
      cursor = formal.find()

      for document in cursor:
          index.save_object({
              'objectID': str(document['_id']),
              'field1': document['field1'],
              'field2': document['field2'],
          })

      return {"message": "Data synced successfully"}
    except:
      raise 'There is either no database available or the existing database is empty.'