import pymongo
from algoliasearch.search_client import SearchClient

# 連接 MongoDB
client = pymongo.MongoClient('mongodb://your_mongodb_connection_string')
db = client['your_database']
collection = db['your_collection']
# 連接 Algolia
client = SearchClient.create('your_algolia_app_id', 'your_algolia_api_key')
index = client.init_index('your_algolia_index_name')

# 從 MongoDB 中讀取數據並上傳到 Algolia
cursor = collection.find()

for document in cursor:
    # 在這裡你可以對文檔進行處理，然後上傳到 Algolia 中
    index.save_object({
        'objectID': str(document['_id']),
        'field1': document['field1'],
        'field2': document['field2'],
        # 添加需要在 Algolia 中搜索的字段
    })

# 關閉 MongoDB 連接
client.close()