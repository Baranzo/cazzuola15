from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)


class AddedDocument(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
