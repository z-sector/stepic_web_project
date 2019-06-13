from django.http import HttpResponse, HttpResponseNotFound

def not_found(request):
    return HttpResponseNotFound("Not Found!")

def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")


