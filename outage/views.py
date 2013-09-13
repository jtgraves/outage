from django.conf import settings
from outage.models import ShutDown, DB_OUTAGE_MSG
from django.shortcuts import redirect
from django.views.generic.base import TemplateView

#TODO: look at pkg utilities for other options
module_path, ctx_class = settings.OUTAGE_CONTEXT.rsplit('.',1)

module = __import__(module_path, fromlist=[ctx_class])

context = getattr(module, ctx_class)


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
        new_context = context(self.request, ctx)
        return new_context
