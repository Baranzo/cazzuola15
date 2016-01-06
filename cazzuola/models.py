from django.db import models

class Documents(models.Model):

    title = models.TextField()
    url = models.URLField()

class AddedDocuments(models.Model):

    title = models.TextField()
    url = models.URLField()
