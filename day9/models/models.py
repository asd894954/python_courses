from mongoengine import *

connect("Lesson_9")


class User(Document):
    login = StringField(max_length=30)
    password = StringField(max_length=8)
    email = EmailField(unique=True)
    role = StringField()


class Category(Document):
    title = StringField(max_length=255,unique=True)
    description = StringField(max_length=1024)


class Item(Document):
    added_by = ReferenceField(User)
    category = ReferenceField(Category)
    is_avialable = BooleanField(Default=True)
    name = StringField(required=True, max_length=255)
    description = StringField(max_length=2048, required=False)
    weight = FloatField(required=False)


# user_obj = User(login="asd", password="123", email="asd@asd.asd", role="admin")
# user = user_obj.save()
# print(user.id)
#
# cat_obj = Category(title='title',description='description')
# cat = cat_obj.save()
#
# item = {"added_by":user,
#         "category":cat,
#         "name":"name",
#         "description":"description",
#         "weight":95
#         }
#
# new_item = Item(**item).save()

