from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request > response 
def say_hello(request):
    #pull data from database
    #Transform
    # send emails 
    # return HttpResponse('Hello world')
    return render(request, 'hello.html')