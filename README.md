====================
Outage: A Django App To Shut Down Your Django App
====================

This is a simple app that can be used to bring down a PyPE django project by
simply adding an entry to an oracle table.

Quick start
-----------

1. Add "outage" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'outage',
      )

2. Add the outage middleware to your MIDDLEWARE_CLASSES setting like this::

      MIDDLEWARE_CLASSES= (
          ...
          'outage.middleware.OutageMiddleware',
      )

3. Add an OUTAGE_CONTEXT object to your settings.py. This should be a class that carries the core of your page context logic. If not supplied, a default will be used.::

   OUTAGE_CONTEXT = 'path.to.your.desired.context.object'

3. Add an OUTAGE_DEFAULT_REDIRECT to your settings.py. This should be the name url pattern, and will be used to redirect any users attempting to access the outage urls directly, when there is no outage occuring.::

   OUTAGE_DEFAULT_REDIRECT = 'url_name' # e.g.: 'home'

4. Include the outage URLconf in your project urls.py like this::

    url(r'^apps/services/requests/', include(outage.urls)),

5. Run `python manage.py syncdb` to create the outage models.

TODO: add notes about db users
