from flask import render_template, request, redirect, url_for
import dao
from saleapps2.saleapp import app


@app.context_processor
def common_attributes():
    return {
        "categories": dao.load_categories()
    }


@app.route("/")
def index():
    categories = dao.load_categories()
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    products = dao.load_products(q, cate_id)
    return render_template("index.html", products=products)


@app.route("/products/<int:id>")
def product_details(id):
    data = dao.load_products_by_id(id)
    categories = dao.load_categories()
    return render_template("product_details.html", data=data)


@app.route("/login", methods=['get', 'post'])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == 'admin' and password == '123':
            return redirect("/")
        else:
            return redirect(url_for("success", name="Anonymous"))

    return render_template("login.html")



if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
