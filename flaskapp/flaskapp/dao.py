import json

def categories_load():
    with open("data/categories.json", encoding="utf-8") as data:
        return json.load(data)


def products_load(q = None, cate_id = None):
    with open("data/products.json", encoding="utf-8") as data:
        products = json.load(data)

        if q !=None :
            products = [p for p in products if p['name'].find(q) >=0]
        if cate_id:
            products = [p for p in products if p['id'] == int(cate_id)]

        return products

if __name__ == "__main__":
    print(products_load())