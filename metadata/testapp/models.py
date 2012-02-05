from django.db import models
from django.contrib.contenttypes import generic
from metadata.models import MetaData

class TestMetaData(models.Model):
    foo = models.CharField(null=True, blank=True, max_length=1)
    metadata = generic.GenericRelation(MetaData)
