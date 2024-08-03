from django.shortcuts import render, redirect
from .models import Categories, Products, Inventory, Salse_customers
from django.contrib import messages
from django.http import HttpResponse
import json

# Create your views here.
def home(request):
    active_home = "active"
    c = Categories.objects.count()
    p = Products.objects.count()

    context = {'active_home':active_home, 'categories':c,"products":p}
    return render(request, 'items/index.html', context)

def categories(request):
    active_categories = "active"
    c = Categories.objects.all()

    context = {"active_categories":active_categories, "categories" : c}
    return render(request, 'items/categories.html', context)

def add_categories(request):
    active_categories = "active"
    context = {"active_categories":active_categories}
    if request.method == "POST":
        Name = request.POST["name"]
        Description = request.POST['description']
        Status = request.POST.get('status', False)
        if Status == 'on':
            Status = True
        else:
            Status = False
        c = Categories(Name = Name, Description = Description, Status = Status)
        c.save()
        messages.success(request, "Categories Added Successfully!")
        return redirect('/categories')
    return render(request, 'items/add_categories.html', context)

def edit_categories(request, itmid):
    active_categories = "active"
    itm = Categories.objects.get(pk = itmid)
    context = {"active_categories":active_categories, 'itm':itm}
    if request.method == "POST":
        Name = request.POST["name"]
        Description = request.POST['description']
        Status = request.POST.get('status', False)

        if Status == 'on':
            Status = True
        else:
            Status = False
        
        itm.Name = Name
        itm.Description = Description
        itm.Status = Status
        itm.save()
        messages.success(request, "Successfully Edited!")
        return redirect("/categories")
    return render(request, "items/edit_categories.html", context)

def delete_categories(request, itmid):
    active_categories = "active"
    itm = Categories.objects.get(pk = itmid)
    itm.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("/categories")




def products(request):
    active_products = "active"
    p = Products.objects.all()
    context = {"active_products":active_products, "products":p}

    return render(request, 'items/products.html', context)

def add_product(request):
    active_products = "active"
    catory = Categories.objects.all()
    context = {"active_products":active_products, 'catory': catory}
    if request.method == "POST":
        Name = request.POST["name"]
        Description = request.POST['description']
        Status = request.POST.get('status', False)
        Price = float(request.POST['price'])
        Categorie = request.POST['categorie']
        cid = Categories.objects.get(Name = Categorie)
        
        if Status == 'on':
            Status = True
        else:
            Status = False

        c = Products(Name = Name, Description = Description, Status = Status, Price = Price, Categorie = cid)
        c.save()
        i = Inventory(Products = c)
        i.save()
        
        messages.success(request, "Product Added Successfully!")
        return redirect('/products')
    return render(request, 'items/add_product.html', context)
    

def edit_product(request, pro_id):
    active_products = "active"
    pid = Products.objects.get(pk = pro_id)
    catory = Categories.objects.all()

    context = {"active_products":active_products, 'p': pid, 'catory': catory}
    if request.method == "POST":
        Name = request.POST["name"]
        Description = request.POST['description']
        Status = request.POST.get('status', False)
        Price = float(request.POST['price'])
        Categorie = request.POST['categorie']
        cid = Categories.objects.get(Name = Categorie)
        
        if Status == 'on':
            Status = True
        else:
            Status = False

        pid.Name = Name
        pid.Description = Description
        pid.Status = Status
        pid.Price = Price
        pid.Categorie = cid

        pid.save()

        messages.success(request, "Product Edited Successfully!")
        return redirect('/products')
    return render(request, 'items/edit_product.html', context)

def delete_product(request, pro_id):
    itm = Products.objects.get(pk = pro_id)
    itm.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("/products")

def inventory(request):
    active_inventory = "active"
    p = Inventory.objects.all()

    context = {"active_inventory":active_inventory, "inventory":p}
    return render(request, 'items/inventory.html', context)
    
def edit_inventory(request, i_id):
    active_inventory = True
    i = Inventory.objects.get(pk = i_id)
    context = {"active_inventory":active_inventory,"i":i}
    if request.method == "POST":
        a = int(request.POST['as'])
        i.Available_Stock = a
        i.save()
        messages.success(request, ' Stock added successfully')
        return redirect('/inventory')
    return render(request, 'items/edit_inventory.html', context)

def sales(request):
    active_sales = "active"
    products = Products.objects.all()
    
    context = {"active_sales":active_sales, 'products':products}
    return render(request, 'items/sales.html', context)
    


def decrement_product(request):
    
    if request.method == "POST":
        product = request.POST.get('product')
        qtl = request.POST.get('qtl', 0)

        l = Products.objects.get(Name = product)
        astock = Inventory.objects.get(Products = l)
        
        if astock.Available_Stock >= int(qtl):
            print("BIG")
            print(astock.Available_Stock , int(qtl))
            astock.Available_Stock -= int(qtl)
            astock.save()
            print('success')
        elif astock.Available_Stock < int(qtl):
            print(astock.Available_Stock , int(qtl))
            print("small")

        
            return HttpResponse('false')
        
        else:
            print('error')
            messages.error(request, "Stock not avaliable")
            return render(request, 'items/sales.html')
            return HttpResponse('true')
            
    return HttpResponse('true')
        


def sales_form(request):
    if request.method =="POST":
        customer_name = request.POST['customer_name']
        total_price = request.POST['total_price']
        total_qtn = request.POST['total_qtn']
        sale_list_json = request.POST['sale_list_json']
        print(json.loads(sale_list_json).items)
        s = Salse_customers(Transaction_code = "Transaction_code",Customers_name = customer_name, Total_items = total_qtn, Total_ammount = total_price, product_bil_data = sale_list_json)

        s.save()
        # messages.success('Data saved successfully')
        return HttpResponse('Data submited successfully')
    return HttpResponse('Somthing wrong!')
    

def invoices(request):
    active_invoices = "active"
    s = Salse_customers.objects.all()
    context = {"active_invoices":active_invoices, "salse_details":s}
    return render(request, 'items/invoices.html', context)
    
def Invoices_details(request, i_id):
    active_invoices = "active"
    s = Salse_customers.objects.get(pk = i_id)
    
    context = {"active_invoices":active_invoices, "salse_details":s}
    return render(request, 'items/invoices_details.html', context)

def delete_invoices(request, i_id):
    s = Salse_customers.objects.get(pk = i_id)
    s.delete()
    return redirect('/invoices')
    