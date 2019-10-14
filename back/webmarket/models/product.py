from peewee import *

from .database import db


class Product(Model):
    id = PrimaryKeyField()
    name = CharField()
    instruction = CharField()
    #description = CharField()
    price = FloatField()
    #stock=IntegerField()
    sprite=CharField(null=True)
    taste=CharField(null=True)
    internal_id=IntegerField()
    detail=CharField()

    class Meta:
        database = db
        schema = 'public'

    def get_categorie_name(self):
        names = []
        for product_category in self.category:
            names.append(product_category.category.name)
        return names

    def get_small_data(self):
        return {'name': self.name, 'categories': self.get_categorie_name(), 'sprite': self.sprite}



with db:
    Product.create_table(fail_silently=True)



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
