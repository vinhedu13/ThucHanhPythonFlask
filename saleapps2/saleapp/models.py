from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from saleapp import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(100), nullable=True)
    products = relationship('Product', backref='category', lazy=True)
    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=False)
    price = Column(Float, default=0)
    image = Column(String(200), default= "https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp")
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    active = Column(Boolean, default=True)

    def __str__(self):
        return self.name

class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    avatar = Column(String(200), default= "https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp")

    def __str__(self):
        return self.name

if __name__ == "__main__":

    # with app.app_context():
    #     #db.create_all()
    #     c = Category(name="Mobile")

    #     import json
    #     with open("data/products.json", encoding="utf-8") as f:
    #         products = json.load(f)
    #         for p in products:
    #             prod = Product(**p)
    #             db.session.add(prod)
    #     db.session.commit()
