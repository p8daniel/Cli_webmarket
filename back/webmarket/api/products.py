from flask import request
from flask_restful import Resource

from webmarket.managers.products import search_products, get_product_by_name, add_new_product, delete_product
from webmarket.managers.categories import get_list_categories

class Products(Resource):
    def get(self):
        query = request.args['query']
        query2 = request.args['query2']
        products_matching = search_products(query,query2)
        products = [product.get_small_data() for product in products_matching]
        # print(products)
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

class Categories(Resource):
    def get(self):
        categories=get_list_categories()
        return categories