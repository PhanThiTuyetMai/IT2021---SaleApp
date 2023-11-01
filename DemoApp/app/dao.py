from DemoApp.models import Category, Product

def load_categories():
    return Category.query.all()


def load_products(kw=None):
    products = Product.query

    return products.all()

