from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    impact = models.TextField()
    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=300)
    projectkeyaspects = models.TextField()
    impact = models.TextField()
    link = models.URLField(blank=True)
    def __str__(self):
        return self.name


