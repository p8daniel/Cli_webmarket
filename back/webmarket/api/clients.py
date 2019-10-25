from flask import request
from flask_restful import Resource


from webmarket.managers.clients import register_new_client, add_product_to_basket, add_new_avis
from webmarket.managers.products import get_product_by_name


class Basket(Resource):
    def put(self):
        product_name=request.json['product']
        taste_name=request.json['taste']
        basket_name=request.json['basket']
        client_name = request.json['client']
        product=get_product_by_name(product_name)
        add_product_to_basket()
