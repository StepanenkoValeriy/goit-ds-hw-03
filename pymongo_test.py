from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://valer4a:Mymongodb2024@cluster0.pyoedqz.mongodb.net/",
    server_api=ServerApi('1')
)

db = client.book

result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

print(result_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)

def read_all():
    cats = db.cats.find()
    for cat in cats:
        return cat 

def read_one(name):
    cat = db.cats.find_one({"name": name})
    if cat:
        print (cat)
    else:
        print("Кота з таким ім'ям не знайдено")

def update_age(name, new_age):
    update_cat = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    return update_cat

def update_features(name, new_features):
    update_cat2 = db.cats.update_one({"name": name}, {"$set": {"features": new_features}})
    return update_cat2

def delete_one(name):
    deleted_cat = db.cats.delete_one({"name": name})
    print("Запис про кота з ім'ям {} видалено")

def delete_all():
    db.cats.delete_many({})
    print("Всі записи видалено")

print (read_all)
print(read_one("barsik"))
print(update_age("barsik", 6))
print(update_features("barsik", "обдирає меблі"))
print(delete_one("barsik"))
print(delete_all)