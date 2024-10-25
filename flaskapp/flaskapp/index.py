from flaskapp import app
from flask import Flask, render_template, request
import dao


@app.route("/")
def home():
    data = dao.categories_load()
    q = request.args.get("a")
    cate_id = request.args.get("category_id")
    products = dao.products_load(q, cate_id)
    return render_template("index.html", data = data, products = products)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)