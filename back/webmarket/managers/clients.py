from webmarket.models.client import *
from webmarket.models.product import *


def add_new_avis(produit, user, avis):
    newavis=Avis.get_or_none(client=user, product=produit)
    if newavis is None:
        Avis.create(client=user, product=produit, text=avis)
    else:
        Avis.update(client=user, product=produit, text=avis)


def register_new_client(nom, prenom, sexe, age, mail):
    newclient=Client.get_or_none(mail=mail)
    if newclient is None:
        Client.create(name=nom, surname=prenom, gender=sexe, age=age)
    else:
        Client.update(name=nom, surname=prenom, gender=sexe, age=age)


def add_product_to_basket(nom_panier, nom_produit, client_email):
    thisbasket=Panier.get_or_none(name=nom_panier)
    if thisbasket is None:
        thisclient=Client.get(mail=client_email)
        if thisclient is None:
            error="The client do not exist"
            return error
        else:
            thisbasket=Panier.create(name=nom_panier, mail=client_email)


    thisproduct=Product.get_or_none(name=nom_produit)
    if thisproduct is None:
        print("The product do not exist")
    else:
        productpanier=PanierProduct.get_or_none(panier=thisbasket, product=thisproduct)
        if productpanier is None:
            PanierProduct.create(panier=thisbasket, product=thisproduct, number_products=1)

        else:
            productpanier.number_products=productpanier.number_products+1
            productpanier.save()
            #productpanier= PanierProduct.update(number_products=actualnumber+1)

        thisbasket.total=thisbasket.total + thisproduct.price


def make_facture(nom_panier):
    actualbasket=Panier.get_or_none(name=nom_panier)
    if actualbasket is None:
        print("basket o not exist")
    else:
        Facture.create()
        print("Facture created")


def add_dicount_to_backet(nom_panier,code):
    actualbasket=Panier.get_or_none(name=nom_panier)
    if actualbasket is None:
        print("The basket do not exist or is empty")
    else:
        actualdiscount=Discount.get_or_none(codename=code)
        if actualdiscount is None:
            print("Discount code not found")
        else:
            actualbasket.total=actualbasket.total*(1-actualdiscount.amount)

def add_discount_code(code, discount_amount):
    Discount.create(name=code, amount=discount_amount)


def get_client_by_name():
    pass