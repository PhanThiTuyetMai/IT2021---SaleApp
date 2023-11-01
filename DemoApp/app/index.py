from flask import render_template, request
import DemoApp, dao
from DemoApp.app import app


@app.route('/')
def index():
    kw = request.args.get('kw')
    cates = dao.load_categories()
    products = dao.load_products(kw)
    return render_template('index.html', categeries=cates, products=products)


if __name__ == '__main__':
    app.run(debug=True)
