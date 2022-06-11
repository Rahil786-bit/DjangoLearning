from django.urls import path
from Blog.views import (article_create_form ,
                        home_blog_view ,
                        article_list_view,
                        dynamic_article_view,
                        update_article,article_delete_view,about_blog_view)

app_name = 'Blog'
urlpatterns = [
    path('create_article', article_create_form,name= 'Article-form'),
    path('', home_blog_view,name= 'Article-Welcome'),
    path('about', about_blog_view,name= 'Article-about'),
    path('list_article', article_list_view,name= 'Article-List'),
    path('<int:my_id>/',dynamic_article_view, name='Article-details'),
    path('update_article/<int:my_id>/',update_article, name='Article-update'),
    path('delete_article/<int:my_id>/',article_delete_view, name='Article-delete'),

]