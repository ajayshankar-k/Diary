from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=500,default='Title...')
    date = models.DateField(blank=True,null=True)
    context = models.TextField()
    email = models.EmailField()
    def __str__(self):
        return self.email


# Create your models here.
