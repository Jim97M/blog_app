from django.shortcuts import render

# Create your views here.
def homepage(request):
    html = <h1>homepage</h1>
    return HttpResponse(html)