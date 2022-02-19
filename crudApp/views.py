from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Customer
from .forms import CustomerForm
# Create your views here.

# class IndexView(TemplateView):
#     template_name = "index.html"

def postData(request):
    if request.method == "POST":
        cust = CustomerForm(request.POST)
        if cust.is_valid():
            cust.save()
            return redirect("/")
        else:
            cust = CustomerForm()

def getData(request):
    custDtl = Customer.objects.all()
    return render(request, "index.html",{'custInfo':custDtl})

def deleteData(request, id):
    custOut = Customer.objects.get(id = id)
    custOut.delete()
    return redirect('/')

def editData(request ,id):
    custEdt = Customer.objects.get(id=id)
    return render(request, "edit.html",{'edtCust':custEdt})

def updateData(request, id):
    if request.method =="POST":
        custData = Customer.objects.get(id=id)
        custForm = CustomerForm(request.POST, instance=custData)
        if custForm.is_valid():
            custForm.save()
            return redirect("/")
    else:
        custForm = CustomerForm() 