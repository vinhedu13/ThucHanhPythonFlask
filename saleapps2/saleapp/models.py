from sqlalchemy import Column, Integer, String
from saleapps2.saleapp import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(100), nullable=True)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        db.create_all()