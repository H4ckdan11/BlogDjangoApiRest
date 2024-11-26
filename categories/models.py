from django.db import models

# Create your models here.
class Categorie(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    published = models.BooleanField(max_length=False)

    def __str__(self):
        return self.title
