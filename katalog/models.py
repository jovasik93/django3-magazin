from django.db import models
from django.urls import reverse


class Towar(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True)
    image = models.ImageField(upload_to='katalog/images/')
    url = models.URLField(blank=True)
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})