from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    """Shows the main page"""

    ## Delete customer
    if request.POST:
        if request.POST['action'] == 'delete':
            Customers.objects.get(customerid=request.POST['id']).delete()

    ## Use ORM to get all objects
    customers = Customers.objects.all().order_by('customerid')
    result_dict = {'records': customers}

    return render(request,'app/index.html',result_dict)

# Create your views here.
def view(request, id):
    """Shows the main page"""
    
    ## Use ORM to get all objects
    customer = Customers.objects.filter(customerid=id).first()
    result_dict = {'cust': customer}

    return render(request,'app/view.html',result_dict)

# Create your views here.
def add(request):
    """Shows the main page"""

    # dictionary for initial data with
    # field names as keys
    context ={}


    # pass the object as instance in form
    form = CustomerForm(request.POST or None)
 
    status = ''
    # save the data from the form
    if form.is_valid():
        form.save()        
        return redirect('index')    

    form = CustomerForm(request.POST or None)

    context["status"] = status
    context["form"] = form
 
    return render(request, "app/add.html", context)

# Create your views here.
def edit(request, id):
    """Shows the main page"""

    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = Customers.objects.filter(customerid=id).first()

    # pass the object as instance in form
    form = CustomerForm(request.POST or None, instance = obj)
 
    status = ''
    # save the data from the form
    if form.is_valid():
        form.save()        
        status = 'Customer edited successfully!'

    form = CustomerForm(request.POST or None,  instance = obj)

    context["obj"] = obj
    context["status"] = status
    context["form"] = form
 
    return render(request, "app/edit.html", context)