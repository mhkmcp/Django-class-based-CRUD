from django.db import models


class Credential(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)