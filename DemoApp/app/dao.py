def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id': 2,
        'name': 'Tablet'
    }]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'IPHONE 13',
        'price': 20000000,
        'image': 'https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg'
        },
        {
            'id': 2,
            'name': 'SAMSUNG A23',
            'price': 20000000,
            'image': 'https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg'
        },
        {
            'id': 3,
            'name': 'IPHONE 15',
            'price': 20000000,
            'image': 'https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg'
        },
        {
            'id': 4,
            'name': 'OPPO 13',
            'price': 20000000,
            'image': 'https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg'
        },
        {
            'id': 5,
            'name': 'IPONE 20',
            'price': 20000000,
            'image': 'https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg'
        },
        {
            'id': 6,
            'name': 'IPHONE 30',
            'price': 20000000,
            'image': 'https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg'
        }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products

