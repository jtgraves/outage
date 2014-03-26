import sys

from cx_Oracle import DatabaseError
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from utdirect.templates import UTDirectContext
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
            request.path == reverse('db_outage') or
            u'static' in request.path.split('/')
            ):
            return None

        try:
            if ShutDown.objects.count() == 1:
                return redirect('outage')
        except DatabaseError as exc:
            return self.process_exception(request, exc)

        return None

    def process_exception(self, request, exception):
        if isinstance(exception, DatabaseError):
            msg = exception.__str__()
            return redirect('db_outage')

