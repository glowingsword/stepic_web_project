from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect

# Create your views here.

from django.http import HttpResponse 

def test(request, *args, **kwargs):
    #return HttpResponse('OK')
    return render(request,'index2.html')
def page404(request, *args, **kwargs):
    raise Http404

def question(request, id):
   return render(request,'index.html',{'id': id,})
