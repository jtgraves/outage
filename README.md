Outage: _A Django App To Shut Down Your Django App_
=====

This is a simple app that can be used to bring down a PyPE django project by
simply adding an entry to an oracle table.

Usage
=====

To include this app in your PyPE project, simply pull it into your project via svn:externals.

> path: extra/outage

> URL: https://github.com/UT-Austin-FIS/outage/tags/1.2/outage

Setup
------

1. Add "outage" to your INSTALLED_APPS setting like this::

```python
      INSTALLED_APPS = (
          ...
          'outage',
      )
```

2. Add the outage middleware to your MIDDLEWARE_CLASSES setting like this::

```python
      MIDDLEWARE_CLASSES= (
          ...
          'outage.middleware.OutageMiddleware',
      )
```

3. Add an OUTAGE_CONTEXT object to your settings.py. This should be a class that carries the core of your page context logic. If not supplied, the UTDirectContext will be used, but you will need to supply the api key in your settings (eg: API_KEY = 'your_api_key')::

```python
   OUTAGE_CONTEXT = 'path.to.your.desired.context.object'
```

4. Add an OUTAGE_DEFAULT_REDIRECT to your settings.py. This should be the name url pattern, and will be used to redirect any users attempting to access the outage urls directly, when there is no outage occuring.::

```python
   OUTAGE_DEFAULT_REDIRECT = 'url_name' # e.g.: 'home'
```

5. Include the outage URLconf in your project urls.py like this::

```python
    url(r'^apps/services/requests/', include(outage.urls)),
```

6. Run `python manage.py syncdb` to create the outage models.


**NOTE**: 
_Since this app creates a new table, if your database design involves multiple users, you will need to go through the same process that you typically use to migrate a table and grant privileges._
