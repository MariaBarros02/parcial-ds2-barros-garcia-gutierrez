from pymongo import MongoClient

client = MongoClient ('mongodb://admin:123456@127.0.0.1:27017/')
db = client.huilasoft_bd;

defectos = db.defectos.find();

semanas = [defectos["semana"] for defecto in defectos]
print(semanas)


