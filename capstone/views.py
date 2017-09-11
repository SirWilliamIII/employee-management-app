from django.http import HttpResponse
from django.shortcuts import render

import datetime


def index(request):
    return render(request, 'index.html', {})


def my_profile(request, pk):
    return HttpResponse('<h1>This is a function based view %s</h1>' % pk)


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
