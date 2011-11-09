from django.conf import settings
from django.utils.encoding import smart_unicode
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from celery.task import task

@task
def add(x, y):
    return x + y
