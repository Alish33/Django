from unicodedata import name
from django.urls import path
from .views import deleteData, postData,getData,editData,updateData
urlpatterns = [
    path("",getData, name="index"),
    path("register",postData,name="regCustomer"),
    path('edit/<int:id>',editData, name="editCustomer"),
    path('update/<int:id>',updateData,name="updateCustomer"),
    path('delete/<int:id>',deleteData, name="deleteData")
]
