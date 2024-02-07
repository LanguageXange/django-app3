from django import forms 
from .models import Link 

# first solution - import this in `views.py`
# class LinkForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     url = forms.URLField(max_length=200)
#     slug = forms.SlugField(required=False)

# second solution with ModelForm
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link 
        fields = ['name','url','slug']