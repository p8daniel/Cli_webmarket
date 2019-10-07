from flask import request
from flask_restful import Resource

from webmarket.managers.products import search_products, get_product_by_name, add_new_product, delete_product


class Products(Resource):
    def get(self):
        query = request.args['query']
        products_matching = search_products(query, type=None)
        products = [product.get_small_data() for product in products_matching]
        return products
    def post(self):
        data = request.json
        product= add_new_product(data['name'], data['price', '', ''])
        return product.get_small_data()

#       def add_new_product(name, price, category, instruction):  # instruction is optional



class Product(Resource):

    def get(self, product_name):
        product = get_product_by_name(product_name)
        return product.get_small_data()

    def delete(self, product_name):
        result = delete_product(product_name)
        return result