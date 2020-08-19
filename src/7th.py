"""from tinydb.storages import MemoryStorage
db = TinyDB(storage=MemoryStorage) # 메모리 방식으로 DB만들기"""


from tinydb import TinyDB, Query
db = TinyDB(‘data.json‘) # JSON 파일형식으로 DB만들기

