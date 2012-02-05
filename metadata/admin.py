from metadata.models import MetaData
from django.contrib.contenttypes import generic

class MetaDataTabularInline(generic.GenericTabularInline):
    model = MetaData
    
class MetaDataStackedInline(generic.GenericStackedInline):
    model = MetaData