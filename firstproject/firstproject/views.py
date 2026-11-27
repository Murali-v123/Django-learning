from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={"name":"murali","place":"usa"}
    return render(request,"index.html",params)
    # return HttpResponse("Hii helllo")

def hello(request):
    return HttpResponse("Hey haiiii kaise hey <a href='/'>back</a>")

def reverse(request):
    return HttpResponse("go back <a href='/'>back</a>")