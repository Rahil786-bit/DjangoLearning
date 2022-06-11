from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "My Title"
    }))
    Content = forms.CharField(required=True,
                                  widget=forms.Textarea(attrs={
                                      "class": "new-class-name two",
                                      "rows": 20,
                                      "cols": 100,
                                      "placeholder": "My Description"
                                  }))
    Vote = forms.IntegerField()
    author =forms.CharField(required=False)
    active = forms.BooleanField()
    class Meta:
        model = Article
        fields = [
            'title',
            'Content',
            'Vote',
            'author',
            'active'

        ]