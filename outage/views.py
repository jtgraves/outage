from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from utdirect.templates import UTDirectContext, UTDirectTemplateAPIError

from outage.models import ShutDown

try:
    module_path, ctx_class = settings.OUTAGE_CONTEXT.rsplit('.',1)
    module = __import__(module_path, fromlist=[ctx_class])
    context = getattr(module, ctx_class)
except AttributeError:
    context = UTDirectContext


class Outage(TemplateView):
    template_name = 'outage.html'

    def get(self, *args, **kwargs):
        objects = ShutDown.objects.all()
        if objects.count() != 1:
            return redirect(settings.OUTAGE_DEFAULT_REDIRECT)

        return super(Outage, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(Outage, self).get_context_data(**kwargs)
        objects = ShutDown.objects.all()
        msg = objects[0].message
        ctx.update({'msg':msg, 'title':'Service Outage'})
        try:
            new_context = context(self.request, ctx)
        except UTDirectTemplateAPIError:
            try:
                new_context = context(
                    self.request,
                    dict=ctx,
                    api_key=settings.API_KEY,
                    page_title='Service Outage',
                    window_title='Service Outage',
                )
            except AttributeError:
                raise ImproperlyConfigured(
                    'If you do not supply your own context object by setting '
                    'an OUTAGE_CONTEXT in settings.py, then you must supply an '
                    'API_KEY in your settings, which will be used to call the '
                    'default UTDirecrContext.'
                )

        return new_context
