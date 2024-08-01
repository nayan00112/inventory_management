from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    
    path("categories", views.categories, name='categories'),
    path("add_categories", views.add_categories, name='add_categories'),
    path("edit_categories/<int:itmid>/", views.edit_categories, name='edit_categories'),
    path("delete_categories/<int:itmid>/", views.delete_categories, name='delete_categories'),

    path("products", views.products, name='products'),
    path("add_product", views.add_product, name='add_product'),
    path("edit_product/<int:pro_id>/", views.edit_product, name='edit_product'),
    path("delete_product/<int:pro_id>/", views.delete_product, name='delete_product'),
    
    path("inventory", views.inventory, name='inventory'),
    path("edit_inventory/<int:i_id>/", views.edit_inventory, name='edit_inventory'),


    path("sales", views.sales, name='sales'),
    path("submit_sales_form", views.sales_form, name='submit_form'),
    path("decrement_product", views.decrement_product, name='decrement_product'),

    path("invoices", views.invoices, name='invoices'),
    path("Invoices_details/<int:i_id>/", views.Invoices_details, name='Invoices_details'),
    path("delete_invoices/<int:i_id>/", views.delete_invoices, name='delete_invoices'),
]
