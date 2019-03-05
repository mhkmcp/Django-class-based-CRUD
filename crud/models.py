from django.db import models
from django.urls import reverse


class Credential(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def get_absolute_url(self):
    	return reverse('crud:index', kwargs={'pk': self.pk})