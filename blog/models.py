from django.db import models
from froala_editor.fields import FroalaField
from .helpers import *

# Create your models here.
class modelBlog(models.Model):
    title = models.CharField(max_length=1000)
    intro = models.CharField(max_length=1000,null = True)
    content = FroalaField()
    slug = models.SlugField(max_length=1000,null = True, blank=True)
    image = models.ImageField(upload_to="blog")
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = generate_slug(self.title)
        super(modelBlog,self).save(*args, **kwargs)


