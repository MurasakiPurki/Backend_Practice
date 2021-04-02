from django.db import models

# Create your models here.
class Blog_post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    content = models.TextField()
    name = models.TextField()
    password = models.TextField()
    