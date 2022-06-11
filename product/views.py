from django.http import Http404
from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


# def product_create_view(request):  #pure Django form saving values
#     form = RawProductForm()
#     if request.method =="POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)   #saving it to our model
#         else:
#             print(form.errors)
#     context = {
#         "form": form
#     }
#     return render(request, "products/product_create.html", context)

def product_create_view(request): #easy way to store form in object admin
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form =ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


# def product_detail_view(request):    #getting object Product from database
#     obj = Product.objects.get(id=3)
#     # context = {
#     #     "title": obj.title,
#     #     "description": obj.description
#     # }
#     context = {
#         'object':obj
#     }
#     return render(request, "products/product_details.html", context)

def dynamic_lookup_view(request,my_id):  #Dynamically getting object from database
    # obj= Product.objects.get(id=my_id)
    obj=get_object_or_404(Product, id=my_id)
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context= {
        "object":obj
    }
    return  render(request,"products/product_details.html", context)

def product_delete_view(request,my_id): # Deleting Object from database
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../home/")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context={
        "object_list":queryset
    }
    return render(request, "products/product_list_view.html", context)
