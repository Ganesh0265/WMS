from django.db import models
import string, random

def generate_unique_code():
    length=6
    while True:
        tag=''.join(random.choices(string.ascii_uppercase, k=length))
        if Item.objects.filter(tag=tag).count()==0:
            break
    return tag

# Create your models here.
class Item(models.Model):
    tag=models.CharField(max_length=8, default="",unique=True)
    name= models.CharField(max_length=40)
    created_at=models.DateTimeField(auto_now_add=True)