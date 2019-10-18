from peewee import *

from .database import db


class Product(Model):
    id = PrimaryKeyField()
    name = CharField()
    instruction = CharField(null=True)
    #description = CharField()
    price = FloatField()
    #stock=IntegerField()
    sprite=CharField(null=True)

    detail=CharField(null=True)


    class Meta:
        database = db
        schema = 'public'

    def get_categorie_name(self):
        names = []
        for product_category in self.category:
            names.append(product_category.category.name)
        return names

    def get_small_data(self):
        return {'name': self.name, 'categories': self.get_categorie_name(), 'sprite': self.sprite,
                 'detail': self.detail}

# 'price': self.price, 'taste': self.taste, 'stock': self.stock, 'label': self.label


with db:
    Product.create_table(fail_silently=True)


class Taste(Model):
    id=PrimaryKeyField
    name=CharField(null=True)
    stock=IntegerField()
    label=CharField(null=True)
    product_id=ForeignKeyField(Product, backref='tastes')
    internal_id = IntegerField()


    class Meta:
        database = db
        schema = 'public'






class Category(Model):
    id = PrimaryKeyField()
    name = CharField()
    #url = CharField()

    class Meta:
        database = db
        schema = 'public'



class ProductCategory(Model):
    id = PrimaryKeyField()
    product = ForeignKeyField(Product, backref='category')
    category = ForeignKeyField(Category, backref='products')
    #is_hidden = BooleanField()
    #slot = IntegerField()

    class Meta:
        database = db
        schema = 'public'




with db:
    # Ability.create_table(fail_silently=True)
    # PokemonAbilities.create_table(fail_silently=True)
    Category.create_table(fail_silently=True)
    ProductCategory.create_table(fail_silently=True)
    Taste.create_table(fail_silently=True)
