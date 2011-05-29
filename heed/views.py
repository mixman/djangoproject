from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

def index(request, template='index.html'):
    data = {}
    return render_to_response(template, RequestContext(request, data))