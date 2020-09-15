from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index( request):
    return render(request,'web/index.html')


def about(request):
    return render(request, 'web/about.html')

# def contact(request):
#
#     messages.success(request, 'Welcome to the My Website.')
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         content = request.POST['content']
#
#         if len(name) < 2 or len(email) < 3 or len(phone) < 11 or len(content) < 4:
#             messages.error(request, "please fill the form correctly")
#
#         else:
#             contact = Contact(name=name, email=email, phone=phone, content=content)
#             contact.save()
#             messages.success(request, "Your message has been sent successfully")
#
#
#     return render(request, 'web/contact.html')
def contact(request):
    # when we want to submit data use POST method and when we want to fetch data use GET method

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 11 or len(content) < 4:
            messages.error(request, "please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent successfully")

    return render(request, 'web/contact.html')

def services(request):
    return render(request, 'web/services.html')
