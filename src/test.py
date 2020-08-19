from tinydb import TinyDB, Query

filepath = "test-tynydb.json"
db= TinyDB(filepath)

table = db.table('fruits')

table = db.table('fruits')

table.insert({'name':})

print(table.all())

Item = Query