from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.


def setcookie(request):
    response=render(request,'setcookie.html')
    response.set_signed_cookie('name','cookie_testing',expires=datetime.utcnow()+timedelta(days=10),salt='sm')
    return response

def getcookie(request):
    nm=request.get_signed_cookie('name',salt='sm')
    return render(request,'getcookie.html',{'cookie':nm})


def deletecookie(request):
    response=render(request,'delcookie.html')
    response.delete_cookie('name')
    return response