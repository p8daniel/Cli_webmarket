# import requests
import csv
# import re

from webmarket.models.product import Product, ProductCategory, Category, Taste


def get_product_by_name(name):
    product = Product.get(name=name)
    return product


def loadfiledata(name="./webmarket/dati_review141019.csv"):
    with open(name, 'r') as f:
        reader=csv.DictReader(f)
        #dict=[]
        for row in reader:
            #print(row)

            name = row['name']
            #name = re.sub(' ', '_', name)
            price = row['price']
            category = row['category']

            sub_name=row['sub_name']
            taste=row['taste']
            sprite=row['sprite']
            internal_id=row['internal_id']
            stock=row['stock']
            label=row['label']
            #category = re.sub(' ', '_', category)

            #dict={'name':row['name'], 'price': row['price'], 'category':row['category'] }
            print(name, price, category, sub_name, taste, sprite, internal_id, stock, label)
            add_new_product(name, price, category, sub_name, taste, sprite, internal_id, stock, label)

# def get_products_by_price(min_price):
#     results = []
#     products = Product.select()
#     for product in products:
#         if product.price <= min_price:
#             results.append(product)
#     return results

def get_products_by_category(category):
     results = []

     mycategory = Category.get(name=category)
     products = Product.select()
     for product in products:
         for a in product.category:
             if a.category == mycategory:
                results.append(product)
     return results


def add_new_product(name,price,category,sub_name,taste,sprite,internal_id,stock,label, instruction="No instructions"): #instruction is optional
    """ create a new product in the database"""


    product=Product.get_or_none(name =name) # first name is class parameter, second is the name form the argument


    if product is None:
        product = Product.create(name=name, instruction=instruction, detail=sub_name, sprite=sprite)
        Taste.create(name=taste, price=price, internal_id=internal_id, stock=stock, label=label, product_id=product)

    else: #the product already exit -> we update it

        tastelem=Taste.get_or_none(internal_id=internal_id)
        if tastelem is None:
            Taste.create(name=taste, price=price, internal_id=internal_id, stock=stock, label=label, product_id=product)
        else:
            Taste.update(name=taste, price=price, internal_id=internal_id, stock=stock, label=label, product_id=product)
        ProductCategory.delete().where(ProductCategory.product == product).execute() # find the productcategory element associated with the product
        product.update(name=name, instruction=instruction, detail=sub_name, sprite=sprite)


    # correspond to the two options (if and else)
    query = Category.get_or_none(name=category)
    if query is None:
        query = Category.create(name=category)
    ProductCategory.create(product=product, category=query)  # like join two table in another table
    print(product.name)
    return product



def delete_product(product_name):
    product = get_product_by_name(product_name)
    product.delete_instance(recursive=True)
    return True





def search_products(query, category):
    if not query:
        print("Not query...")
        products = Product.select()
        if category:
            #print("ciao")
            filtered_products = []
            for product in products:
                # types = [t.type.name for t in pokemon.types]
                categories = []
                productcategories_de_ce_produit = ProductCategory.select().where(ProductCategory.product == product)
                for productcategory in productcategories_de_ce_produit:
                    category_name = productcategory.category.name
                    categories.append(category_name)

                if category in categories:
                    filtered_products.append(product)
            return filtered_products
    else:
        query = query.lower()
        products = Product.select().where(Product.name.contains(query))
        # for product in products:
        #
        #
        #     print(product.name)

        if category:
            #print("ciao")
            filtered_products = []
            for product in products:
                # types = [t.type.name for t in pokemon.types]
                categories = []
                productcategories_de_ce_produit = ProductCategory.select().where(ProductCategory.product == product)
                for productcategory in productcategories_de_ce_produit:
                    category_name = productcategory.category.name
                    categories.append(category_name)

                if category in categories:
                    filtered_products.append(product)
            return filtered_products
    # for product in products:
    #     print(product.name)
    return products

