from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "My Title"
    }))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={
                                      "class": "new-class-name two",
                                      "rows": 20,
                                      "cols": 100,
                                      "placeholder": "My Description"
                                  }))
    price = forms.DecimalField(initial=199.9)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not a Valid Title")

class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"My Title"
    }))
    description = forms.CharField(required=False,
        widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "rows": 20,
        "cols": 100,
         "placeholder": "My Description"
    }))
    price = forms.DecimalField(initial=199.9)
