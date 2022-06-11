from django.shortcuts import render , get_object_or_404 ,redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.

def article_create_form(request):
    form = ArticleForm(request.POST or None)
    form.author = request.user.username
    if form.is_valid():
        #form.author =request.user.username
        form.save()
        #form = ArticleForm()
        messages.success(request,'Your Article has been Saved Successfully!')
        return HttpResponseRedirect(reverse_lazy('Article-Welcome'))

    context = {
        'form': form
    }
    return render(request, "Blog/article_form.html", context)

def home_blog_view(request):
    context={}
    return  render(request,"Blog/Blog_welcome.html",context)


def article_list_view(request):
    queryset = Article.objects.all()
    for obj in queryset:
        print(obj.id)
    context={
        "object_list":queryset
    }
    return render(request, "Blog/article_list_view.html", context)

def dynamic_article_view(request,my_id):  #Dynamically getting object from database
    # obj= Product.objects.get(id=my_id)
    obj=get_object_or_404(Article, id=my_id)
    paraObj = obj.Content.split("\n")
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context= {
        "object":obj,
        "para":paraObj
    }
    return  render(request,"Blog/article_view.html", context)



def update_article(request, my_id):
    update_data = Article.objects.get(id=my_id)
    form = ArticleForm(request.POST or None, instance=update_data)
    if form.is_valid():
        form.save()
        #form = ArticleForm()
        messages.success(request,'Your Article '+update_data.title+ ' has been Updated Successfully!')
        return HttpResponseRedirect(reverse_lazy('Article-Welcome'))

    context ={
        "data":update_data,
        "form":form
    }
    return render(request,"Blog/update_article.html",context)


def article_delete_view(request,my_id): # Deleting Object from database
    obj = get_object_or_404(Article, id=my_id)
    deleted_data = Article.objects.get(id=my_id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Your Article ' + deleted_data.title + ' has been Deleted Successfully!')
        return redirect(reverse_lazy('Article-Welcome'))
    context = {
        "object": obj
    }
    return render(request, "Blog/delete_article.html", context)


def about_blog_view(request):
    context={}
    return  render(request,"Blog/about_page.html",context)