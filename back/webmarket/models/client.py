from peewee import *

from .database import db
from .product import Product


class Client(Model):
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    #gender = CharField()
    # age= IntegerField()
    email= CharField()
    password=CharField()


    class Meta:
        database = db
        schema = 'public'



class Avis(Model):
    id=PrimaryKeyField()
    client=ForeignKeyField(Client, backref='avis_clients')
    product=ForeignKeyField(Product, backref='avis_produits')
    text=CharField()

    class Meta:
        database = db
        schema = 'public'


class Facture(Model):
    id=PrimaryKeyField()

    class Meta:
        database = db
        schema = 'public'


class Panier(Model):
    id=PrimaryKeyField()
    name=CharField
    total=FloatField()
    client = ForeignKeyField(Client, backref='paniers_client')
    facture=ForeignKeyField(Facture, backref='paniers')


    class Meta:
        database = db
        schema = 'public'


class PanierProduct(Model):
    id = PrimaryKeyField()
    number_products= IntegerField()
    product=ForeignKeyField(Product, backref='paniers')
    panier= ForeignKeyField(Panier, backref='products')

    class Meta:
        database = db
        schema = 'public'

class Discount(Model):
    id=PrimaryKeyField()
    name=CharField()
    amount=FloatField()
    #panier=ForeignKeyField(Panier, backref='discounts')

    class Meta:
        database = db
        schema = 'public'






