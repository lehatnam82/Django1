from django.db import models

# Create your models here.
class contactForm(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    body = models.TextField(max_length=254,default="")
    def  __str__(self):
        return self.username

