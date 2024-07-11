from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Message, Chat
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from .forms import RegistrationForm



# Create your views here.

@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        print("Received data: " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {"messages": chatMessages})


def login__view(request):
    redirect = request.GET.get('next', '/chat/')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'login/index.html', {'wrongpassword': True, 'redirect': redirect})
    return render(request, 'login/index.html', {'redirect': redirect})

# def register(request):
#     redirect = request.GET.get('next', '/login/')
#     if request.method == 'POST':
#         username_input = request.POST.get('username')
#         password_input = request.POST.get('password')
#         password_check = request.POST.get('password_check')
#         if password_input == password_check:
#             user = User.objects.create_user(username=username_input, password=password_input)
#             user.save()
#             return HttpResponseRedirect(request.POST.get('redirect'))
#         else:
#             return render(request, 'register/register.html', {'password_dont_match': True, 'redirect': redirect, 'wrongpassword': False,  'error': 'it doesnt work', })
#     return render(request, 'register/register.html', {'redirect': redirect,})



def sign_up(request):
    form=RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/chat')
        else:
            form = RegistrationForm()
            print(form.errors)
            
    return render(request, 'register/register.html', {'form':form,})