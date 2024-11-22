import json
from models import *
from saleapp import app
import hashlib

def load_categories():
    # with open("data/categories.json", encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query.all()


def load_products(q=None, cate_id=None, page = None):

    # with open("data/products.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #
    #     if q:
    #         products = [p for p in products if p["name"].find(q) >= 0]
    #     if cate_id:
    #         products = [p for p in products if p["id"].__eq__(int(cate_id))]
    #
    #     return products
    query = Product.query
    if q:
        query = query.filter(Product.name.contains(q))
    if cate_id:
        query = query.filter(Product.category_id.__eq__(int(cate_id)))
    if page:
        page_size = app.config['PAGE_SIZE']
        start = (int(page)-1)*page_size
        query = query.slice(start, start+page_size)

    return query.all()


def count_product():
    return Product.query.count()


def load_products_by_id(id):
    # with open("data/products.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #
    #     for i in products:
    #         if i["id"] == id:
    #             return i
    return Product.query.get(id)

if __name__=="__main__":
    print(load_products())