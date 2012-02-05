__test__ = {"doctest": """
To test metadata we use metadata.testapp, so you must have it in
your INSTALLED_APPS

>>> from metadata.testapp.models import TestMetaData

>>> test = TestMetaData(foo='b')
>>> test.save()
>>> metadata = test.metadata.create(name='twitter_screen_name', value='rafaelsdm')
>>> metadata = test.metadata.create(name='plurk_user', value='pathiene')


Metadata can be used as a read-only dict like object (you can't set
anything by index)
>>> test.metadata['twitter_screen_name']
u'rafaelsdm'
>>> test.metadata['plurk_user']
u'pathiene'
>>> test.metadata.keys()
[u'plurk_user', u'twitter_screen_name']

Always sorted by the name of metadata
>>> test.metadata.values()
[u'pathiene', u'rafaelsdm']

You can also iterate over .[iter]items()
>>> test.metadata.items()
[(u'plurk_user', u'pathiene'), (u'twitter_screen_name', u'rafaelsdm')]

>>> for name, value in test.metadata.iteritems():
...     print name, '=', value
plurk_user = pathiene
twitter_screen_name = rafaelsdm

>>> test.metadata['setitem'] = 'also works'
>>> test.metadata['setitem']
u'also works'

You can even get objects with an specific metadata information
>>> for x in xrange(30):
...     testN = TestMetaData(foo='bar %x'%(x))
...     testN.save()
...     if x%3==0:
...         testN.metadata['has_something'] = 'Y'
...     elif x%10==0:
...         testN.metadata['has_something'] = 'N'
>>> TestMetaData.objects.filter(metadata__name='has_something', metadata__value='Y').count()
10
>>> TestMetaData.objects.filter(metadata__name='has_something', metadata__value='N').count()
2
>>> TestMetaData.objects.filter(metadata__name='has_something').count()
12
"""}

