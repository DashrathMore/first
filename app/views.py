from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse ('<h1><i> My Home in Maharashtra <i></h1>')

def  hometown(request):
    return HttpResponse('<marquee><h1>===============================================================maharashtra...</h1></marquee>')

def friends(request):
    return HttpResponse ('<marquee><h1><i> Hi Friends ..........</i></h1></marquee>')
def boys(request):
    return HttpResponse ('''<marquee><h1><i> The
                                                Boys....
                         </i></h1></marquee>''')