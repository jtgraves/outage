from django.db.models import Model, CharField

DB_OUTAGE_MSG = (
    'This application is experiencing a database problem. The developers have '
    'been notified and are working to resolve it.'
)


class ShutDown(Model):
    # TODO: add start and end times
    message = CharField(max_length=1000)
