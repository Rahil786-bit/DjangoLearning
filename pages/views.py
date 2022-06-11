from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args , **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args , **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args , **kwargs):
    my_context = {
        "my_text" : "Checking the text",
        "my_number" : 8872663,
        "my_list" : [123,456,789],
        "page_name": "Another"
    }
    return render(request, "about.html", my_context)