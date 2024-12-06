from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from saleapp import app, db
from models import Category, Product

admin = Admin(app = app, name="ADMIN WEBSITE", template_mode='bootstrap4')

class MyCategoryView(ModelView):
    column_list = ["name", "products"]

class ProductsView(ModelView):
    column_list = ["id","name", "category_id", "price", "image", "active"]
    column_searchable_list = ["name", "id"]
    column_filters = ['name']


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(ProductsView(Product, db.session))