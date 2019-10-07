import click

from webmarket.managers import products, clients


@click.group()
def cli():
    click.echo('## Webmarket ##')


@cli.group()
def load():
    pass

@load.command('datafile')
@click.argument('name')
def load_file(name):
    products.loadfiledata(name)



@cli.group()
def get():
    pass


@get.command('product')
@click.argument('name')
# @click.option('--abilities', is_flag=True)
# @click.option('--types', is_flag=True)
def get_name(name):
     product = products.get_product_by_name(name) #we call the manager
     click.echo(f'Product {product.name}')
     click.echo(f'Price: {product.price}')
     #click.echo(f'Category: {product.category.name}')
#     if abilities is True:
#         abilities = [a.ability.name for a in product.abilities]
#         click.echo(f'Abilities: {abilities}')
#     if types is True:
#         types = [a.type.name for a in product.types]
#         click.echo(f'Types: {types}')


@get.command('products')

@click.option('--category')
@click.option('--price')

# @click.option('--type')
def get_products(category, price):
    if price is not None:
        products_with_price = products.get_products_by_price(int(price))
        names = [p.name for p in products_with_price]
        click.echo(f'Products : {names}')
    if category is not None:
        products_with_category = products.get_products_by_category(category)
        names = [p.name for p in products_with_category]
        click.echo(f'Products : {names}')

@cli.group()
def add():
    pass


@add.command('product')
@click.argument('name')
@click.argument('price')
@click.argument('category')
@click.argument('instruction')
def add_product(name, price, category, instruction):
    product=products.add_new_product(name, price, category, instruction)
    click.echo(f"{product.name} added to database")

# @click.option('--abilities', is_flag=True)
# @click.option('--types', is_flag=True)
# def load_product(name, abilities, types):
#     product = products.load_product_from_api(name)
#     if abilities:
#         abilities = products.load_product_abilities_from_api(name)
#     click.echo(f'Product loaded: {product.name}')
#     if types:
#         types = products.load_product_types_from_api(name)
#         click.echo(f'Product loaded: {product.name}')


# @load.command('products')
# @click.option('--abilities', is_flag=True)
# @click.option('--types', is_flag=True)
# def load_products(abilities, types):
#     product_number = products.load_all_products_from_api(abilities, types)
#     click.echo(f'Products loaded: {product_number}')


@cli.group()
def search():
    pass


@search.command('products')
@click.argument('query')
def search_products(query):
    products_matching = products.search_products(query)
    names = [p.name for p in products_matching]
    click.echo(f'Products found: {names}')

