from django.db import models
from django.utils.text import slugify

# Create your models here.
# Save a shortened link - name, url, slug, # of clicks;

class Link(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200)
    # example.com/link/name_of_link
    slug = models.SlugField(unique=True, blank=True) # auto generated based on name if not provided
    clicks = models.PositiveIntegerField(default=0) # times the url is clicked

    def __str__(self):
        return f"Name:{self.name} | Click: {self.clicks}"
    
    def click(self):
        self.clicks +=1
        self.save()

    # overwrite save method to auto generate slug if not provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)