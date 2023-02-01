from django.db import models
from django.db.models import Model
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from mindmap import settings

class GroupDocuments(models.Model):
    name = models.TextField(unique=True)
    datetime = models.DateTimeField()
    description = models.TextField()
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.name

def content_file_name(instance, filename):
    return '/'.join(['documents', instance.group_id, filename])

class Document(models.Model):
    document = models.FileField(null=False, upload_to=content_file_name)
    name = models.TextField()
    description = models.TextField()
    datetime = models.DateTimeField()
    group_id = models.TextField()
    def __str__(self):
        return self.name
    
    def get_url(self):
        return self.document.url    

