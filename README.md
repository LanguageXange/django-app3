## Django Bitly Clone

create shorter URLs for any webpage and also track how many clicks each get.
Users will be able to add new links directly from the application.

### Using ModelForm

```
# forms.py
from django import forms
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name','url','slug']

```

### Install Crispy Form

`pip install django-crispy-forms`
`pip install crispy-tailwind`
