from django.db import models

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
