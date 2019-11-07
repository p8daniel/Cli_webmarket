from peewee import *
from playhouse.shortcuts import model_to_dict

from .database import db
from .product import Product

class CommonModel(Model):
    def get_small_data(self):
        return model_to_dict(self, recurse=False, backrefs=False)

    class Meta:
        database = db
        schema = 'client'



class Client(CommonModel):
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    #gender = CharField()
    # age= IntegerField()
    email= CharField()
    password=CharField()
    actual_basket=CharField()



class Avis(CommonModel):
    id=PrimaryKeyField()
    client=ForeignKeyField(Client, backref='avis_clients')
    product=ForeignKeyField(Product, backref='avis_produits')
    text=CharField()



class Facture(CommonModel):
    id=PrimaryKeyField()



class Panier(CommonModel):
    id=PrimaryKeyField()
    name=CharField
    total=FloatField()
    client = ForeignKeyField(Client, backref='paniers_client')
    facture=ForeignKeyField(Facture, backref='paniers')



class PanierProduct(CommonModel):
    id = PrimaryKeyField()
    number_products= IntegerField()
    product=ForeignKeyField(Product, backref='paniers')
    panier= ForeignKeyField(Panier, backref='products')



class Discount(CommonModel):
    id=PrimaryKeyField()
    name=CharField()
    amount=FloatField()
    #panier=ForeignKeyField(Panier, backref='discounts')







