from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length = 120) #max_length = 120
    Content =  models.TextField(blank=True, null = True)
    Vote       = models.IntegerField()
    active    = models.BooleanField(default = True)
    author = models.CharField(max_length=150,null=True)


    def get_absolute_url(self):
        return reverse("Blog:Article-update",kwargs={"my_id":self.id})

    def get_articleDetail_url(self):
        return reverse("Blog:Article-details",kwargs={"my_id":self.id})
    def get_articleDelete_url(self):
        return reverse("Blog:Article-delete",kwargs={"my_id":self.id})