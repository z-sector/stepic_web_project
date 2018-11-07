from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET, require_POST


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def question(request, id):
    return HttpResponse(id)
