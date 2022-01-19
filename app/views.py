from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    """Shows the main page"""

    ## Delete customer request
    if request.POST:
        if request.POST['action'] == 'delete':
            Customers.objects.get(customerid=request.POST['id']).delete()

    ## Use ORM to get all customers ordered by their customer ID
    customers = Customers.objects.all().order_by('customerid')
    result_dict = {'records': customers}

    ## Render the index page
    return render(request,'app/index.html',result_dict)

def view(request, id):
    """Shows the view customer page"""
    
    ## Use ORM to get the customer by their ID
    customer = Customers.objects.filter(customerid=id).first()
    result_dict = {'cust': customer}

    ## Render the view page
    return render(request,'app/view.html',result_dict)

def add(request):
    """Shows the add new customer page"""

    # Dictionary for initial data
    context ={}
    
    ## Pass the object as instance in form
    form = CustomerForm(request.POST or None)
 
    status = ''
 
    ## Save the data from the form
    if form.is_valid():
        form.save()        
        return redirect('index')    

    context["status"] = status
    context["form"] = form
    
    ## Render the add page
    return render(request, "app/add.html", context)

def edit(request, id):
    """Shows the edit customer page"""

    ## Dictionary for initial data 
    context ={}
 
    ## Fetch the customer related with the given customerid
    obj = Customers.objects.filter(customerid=id).first()

    ## Pass the object as instance in form
    form = CustomerForm(request.POST or None, instance = obj)
 
    status = ''
    ## Save the data from the form
    if form.is_valid():
        form.save()        
        status = 'Customer edited successfully!'

    form = CustomerForm(request.POST or None,  instance = obj)

    context["obj"] = obj
    context["status"] = status
    context["form"] = form
    
    ## Render the edit page
    return render(request, "app/edit.html", context)
