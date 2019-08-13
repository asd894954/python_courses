import shelve

db_name = "local.db"

with shelve.open(db_name) as db:
    db["key"] = "Value"

    for c in db:
        print(c, db[c])


def create_item(key, value):
    with shelve.open(db_name) as db:
        db[key] = value


def get_item(key):
    with shelve.open(db_name) as db:
            return db.get(key)


create_item('key1', 'value1')
create_item('key3', [1, 2, 3])

print(get_item('key2'))
