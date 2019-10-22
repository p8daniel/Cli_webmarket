from webmarket.models.product import Category

def get_list_categories(search=None, unused=False):

    if unused:
        categories = [category.name for category in Category.select() if len(category.products) == 0]

    elif search != None:
        categories = [category.name for category in Category.select() if category.products == search]

    else:
        categories = [category.name for category in Category.select()]

    return categories
