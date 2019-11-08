from flask import request
from flask_restful import Resource


from webmarket.managers.clients import register_new_client, add_product_to_basket, add_new_avis, get_client_by_name
from webmarket.managers.products import get_product_by_name


class Basket(Resource):
    def put(self):
        product_name=request.json['product']
        taste_name=request.json['taste']
        basket_name=request.json['basket']
        client_name = request.json['client']
        product=get_product_by_name(product_name)
        add_product_to_basket()


class Client(Resource):
    def put(self, client_name):
        # data = request.json
        register_new_client(client_name)

    def get(self, client_name):
        user = get_client_by_name(client_name)
        if user is None:
            return {'msg': 'Not found'}, 404
        return user.name



class Clients(Resource):
    def get(self):
        pass
