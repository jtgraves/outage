import sys

from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from outage.models import ShutDown

_using_manage = True in ['manage.py' in arg for arg in sys.argv]

TESTING = ((_using_manage and 'test' in sys.argv) or ('nosetests' in sys.argv))


class OutageMiddleware(object):
    def process_request(self, request):

        # Django tests may set their own ROOT_URLCONF, in which case we may not
        # be able to resolve 'outage', so we'll just return None unless testing
        # this app intentionally.
        if TESTING and 'outage' not in sys.argv:
            return None

        if (request.path == reverse('outage') or
            u'static' in request.path.split('/')
            ):
            return None

        if ShutDown.objects.count() == 1:
            return redirect('outage')

        return None

