"""first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from pages.views import home_view , contact_view, about_view
# from Blog.views import  article_create_form ,home_blog_view ,article_list_view ,dynamic_article_view,update_article,article_delete_view

urlpatterns = [
    path('products/', include('product.urls')), # neeed to repeat this scenario
    path('Blog/', include('Blog.urls',namespace="Blog")),
    path('home/',home_view, name='home'),
    # path('about/',about_view, name='About'),
    path('contact/',contact_view, name='Contact'),
    path('admin/', admin.site.urls),
]
