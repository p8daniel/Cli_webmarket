from peewee import *

from .database import db
from playhouse.shortcuts import model_to_dict


class CommonModel(Model):
    def get_small_data(self):
        return model_to_dict(self, recurse=False, backrefs=False)

    class Meta:
        database = db
        schema = 'public'


class Product(CommonModel):
    id = PrimaryKeyField()
    name = CharField()
    instruction = CharField(null=True)
    #description = CharField()
    #stock=IntegerField()
    sprite=CharField(null=True)

    detail=CharField(null=True)



    def get_categorie_name(self):
        return [product_category.category.name for product_category in self.category]

    def get_taste_name(self):
        return [product_taste.name for product_taste in self.tastes]


    def get_small_data(self):
        return {'name': self.name, 'categories': self.get_categorie_name(), 'sprite': self.sprite,
                 'detail': self.detail, 'tastes':self.get_taste_name()}

# 'price': self.price, 'taste': self.taste, 'stock': self.stock, 'label': self.label


with db:
    Product.create_table(fail_silently=True)


class Taste(CommonModel):
    id=PrimaryKeyField
    name=CharField(null=True)
    stock=IntegerField()
    price = FloatField(null=True)
    label=CharField(null=True)
    product_id=ForeignKeyField(Product, backref='tastes')
    internal_id = IntegerField()



    def get_small_data(self):
        return {'name': self.name, 'stock': self.stock, 'price': self.price,
                 'label': self.label}


class Category(CommonModel):
    id = PrimaryKeyField()
    name = CharField()
    #url = CharField()





class ProductCategory(CommonModel):
    id = PrimaryKeyField()
    product = ForeignKeyField(Product, backref='category')
    category = ForeignKeyField(Category, backref='products')
    #is_hidden = BooleanField()
    #slot = IntegerField()





with db:
    Category.create_table(fail_silently=True)
    ProductCategory.create_table(fail_silently=True)
    Taste.create_table(fail_silently=True)
