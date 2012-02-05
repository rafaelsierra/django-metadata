# django-metadata addon

This is a simple addon to your models, with this package you can add metadata to any of your models.

By *metadata* we understand attributes/values that are not commonly shared across all instances of a particular model.

If you have a `Product` model and your instance is about Digital Cameras, you may want store what are it's resolution, storage capacity and lens type, but those informations have nothing to do with a lamp. These informations can easily be stored with `django-metadata`


## Install

Clone django-metadata somewhere:

````bash
git clone git://github.com/rafaelsdm/django-metadata.git
```


Add `django-metadata` into `PYTHONPATH`:

```bash
export PYTHONPATH=$PYTHONPATH:/somewhere/django-metadata
```

Remember to replace `/somewhere/` to the path where you cloned the code.

You can also add the line above into your `~/.bashrc`.

## Using

Import `metadata.models.MetaData` into your `model.py` file and create a `django.contrib.contenttypes.generic.GenericRelation` field where you want to use meta data

```python
# THIS IS JUST AN EXAMPLE
from django.db import models
from django.contrib.contenttypes import generic
from metadata.models import MetaData

class MyModel(models.Model):
    foo = models.CharField(null=True, blank=True, max_length=1)
    metadata = generic.GenericRelation(MetaData)

```

Add `metadata` into your `settings.INSTALLED_APPS`:

```python
# ...
INSTALLED_APPS = (
    ...
    'metadata',
)
# ...
```

Now `manage.py syncdb` your project to create metadata models and have fun using it:

```python
from myapp.models import MyModel
mymodel = MyModel.objects.get(id=1)
mymodel.metadata['something'] = 'some value'
mymodel.metadata['something']
```

Note that `name` and `value` have a limit of 256 characteres, this is to increase performance and allow any database to index it ([PostgreSQL have limit](http://wiki.postgresql.org/wiki/FAQ#What_is_the_maximum_size_for_a_row.2C_a_table.2C_and_a_database.3F) on the size of a VARCHAR field to index it)

metadata manager objects are dict like objects, and implements `__setitem__`, `__getitem__`, `iterkeys`, `keys`, `itervalues`, `values`, `iteritems` and `items`, so you can use them at templates by doing some thing like:
```
{% if mymodel.metadata.something %}
```
So it will check if `mymodel` object has the metadata `something` into it

## Notes

This is not a replacement for fields into models, you should use it when some records have some data that other records (in the same table) have not.

As it's a very simple model with basic usage of GenericRelations and
Manager objects, it works pretty much with all 1.x versions of Django
(so far)
