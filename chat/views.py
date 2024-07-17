from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Message, Chat
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import *
from .forms import RegistrationForm
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import logout
from django.urls import reverse

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    """
    This is a view to render the chat html.
    
    """
    if request.method == 'POST':
        print("Received data: " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [ new_message, ])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {"messages": chatMessages})


def login__view(request):
    redirect = request.GET.get('next', '/chat/')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            request.session['is_logged_in'] = True
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'login/index.html', {'wrongpassword': True, 'redirect': redirect})
    return render(request, 'login/index.html', {'redirect': redirect})


def sign_up(request):
    form=RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['is_logged_in'] = True
            return redirect('/chat')
        else:
            form = RegistrationForm()
            return render(request, 'register/register.html', {'password_dont_match': True,})
            
    return render(request, 'register/register.html', {'form':form,})

def logout_view(request):
    if request.method == 'POST':
        logout(request)  
        request.session['is_logged_in'] = False
        return redirect('login')
     