from flask import Blueprint
from flask_restful import Api

from webmarket.models.database import db

from webmarket.api.products import Product, Products, Categories, Taste
from webmarket.api.clients import Basket, Clients, Client

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# auth= Blueprint('auth', __name__)


def register_api(app):
    @api_bp.before_request
    def before_request():
        db.connect(reuse_if_open=True)

    @api_bp.teardown_request
    def after_request(exception=None):
        db.close()

    api.add_resource(Products, '/products')
    api.add_resource(Product, '/product/<product_name>')
    api.add_resource(Taste, '/product/<product_name>/<product_taste>')
    api.add_resource(Categories, '/categories')
    api.add_resource(Basket, '/basket')
    api.add_resource(Clients, '/clients')
    api.add_resource(Client, '/client/<client_name>')

    app.register_blueprint(api_bp, url_prefix="/api/v1")

# def register_login(app):
#
#
#     app.register_blueprint(auth)
