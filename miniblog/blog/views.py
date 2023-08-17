from django.shortcuts import render, HttpResponseRedirect
from .forms import UserSignUpForm, UserLoginForm, AdPost
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group


def home(request):
    post = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': post})




def user_about(request):
    return render(request, 'blog/about.html')


def user_contact(request):
    return render(request, 'blog/contact.html')


def user_signup(request):
    if request.method == 'POST':
        fm = UserSignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'congratulessions! you have become a Author')
            user = fm.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
            
    else:
        fm = UserSignUpForm()
    return render(request, 'blog/signup.html', {'form': fm })


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserLoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=uname, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "loged in successfully!!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = UserLoginForm()
        return render(request, 'blog/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = AdPost(request.POST)
            if fm.is_valid():
                title = fm.cleaned_data['title']
                desc = fm.cleaned_data['desc']
                pst = Post(title=title , desc=desc)
                pst.save()
                fm = AdPost()
        else:
            fm = AdPost()
        return render(request, 'blog/adpost.html', {'form': fm})


def user_update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            fm = AdPost(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi = Post.objects.get(pk=id)
            fm = AdPost(instance=pi)
        return render(request, 'blog/updatepost.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/dashboard/')

def user_dashboard(request):    
    if request.user.is_authenticated:
        post = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html',{'posts':post , 'username':full_name,
                                                'gps':gps})
    
 