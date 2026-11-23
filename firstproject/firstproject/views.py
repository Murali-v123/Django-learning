from django.http import HttpResponse

def index(request):
    return HttpResponse("Hii helllo")

def hello(request):
    return HttpResponse("Hey haiiii kaise hey")