import requests
import csv
import re

from webmarket.models.product import Product, ProductCategory, Category


def get_product_by_name(name):
    product = Product.get(name=name)
    return product


def loadfiledata(name="/home/daniel/Dropbox/PyCharmLinux/Cli_webmaket/back/webmarket/dati.csv"):
    with open(name, 'r') as f:
        reader=csv.DictReader(f)
        #dict=[]
        for row in reader:
            #print(row)

            name = row['name']
            name = re.sub(' ', '_', name)
            price = row['price']
            category = row['category']
            category = re.sub(' ', '_', category)

            #dict={'name':row['name'], 'price': row['price'], 'category':row['category'] }
            #print(name, price, category)
            add_new_product(name,price,category,"null")

def get_products_by_price(min_price):
    results = []
    products = Product.select()
    for product in products:
        if product.price <= min_price:
            results.append(product)
    return results

def get_products_by_category(category):
     results = []

     mycategory = Category.get(name=category)
     products = Product.select()
     for product in products:
         for a in product.category:
             if a.category == mycategory:
                results.append(product)
     return results


def add_new_product(name, price, category, instruction): #instruction is optional
    """ create a new product in the database"""


    product=Product.get_or_none(name =name) # first name is class parameter, second is the name form the argument


    if product is None:
        product = Product.create(name=name, price=price, instruction=instruction)

    else: #the product already exit -> we update it

        ProductCategory.delete().where(ProductCategory.product == product).execute() # find the productcategory element associated with the product
        product.update(name=name, price=price, instruction=instruction)


    # correspond to the two options (if and else)
    query = Category.get_or_none(name=category)
    if query is None:
        query = Category.create(name=category)
    ProductCategory.create(product=product, category=query)  # like join two table in another table
    print(product.name)
    return product
    print(product.name)


def delete_product(product_name):
    product = get_product_by_name(product_name)
    product.delete_instance(recursive=True)
    return True


def search_products(query):
    query = query.lower()
    products = Product.select().where(Product.name.contains(query))
    return products

#types = [a.type.name for a in product.types]

# def search_types(query):
#     query = query.lower()
#     results = []
#
#     products = Product.select()
#     for product in products:
#         if product.hp >= min_hp:
#             results.append(product)
#
#     return results
#
#     ids = ProductCategories.select().where(ProductTypes.type==query)
#
#     products = Product.select().where(Product.id== ids.id)
#     return products


#query = Typex.select().where(Typex.name == )

#ProductTypes.delete().where(ProductTypes.product == query).execute()