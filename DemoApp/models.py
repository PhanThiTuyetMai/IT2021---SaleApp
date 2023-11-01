from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app import db, app
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product',  backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False )


if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(name='iPhone13', price=19000000, category_id=1,
                     image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')

        p2 = Product(name='SamSung A23', price=20000000, category_id=1,
                     image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')

        p3 = Product(name='Galaxy S20', price=50000000, category_id=2,
                     image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')

        p4 = Product(name='iPad 15', price=25000000, category_id=2,
                     image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')

        p5 = Product(name='Oppo 32', price=28000000, category_id=1,
                     image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')

        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
        #db.create_all()
