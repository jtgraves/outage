from django.core.urlresolvers import reverse
from outage.models import ShutDown
from django.shortcuts import redirect


class OutageMiddleware(object):
    def process_request(self, request):

        if (request.path == reverse('outage') or
            u'static' in request.path.split('/')
            ):
            return None

        if ShutDown.objects.count() == 1:
            return redirect('outage')

        return None
