from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User,auth
from .models import Profile

from contents.models import Post

@ login_required
def favourite_list(request):
    new = Post.newmanager.filter(favourites=request.user)
    return render(request,
                  'accounts/favourites.html',
                  {'new': new})


@ login_required
def favourite_add(request, id):
    post = get_object_or_404(Post, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])




@login_required
def profile(request):
    return render(request,
                  'accounts/profile.html',
                  {'section': 'profile'})

def signup(request):
    if request.method == 'POST':
        username=request.POST['username'] 
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('account:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'User taken') 
                return redirect('account:signup')
            else:
                user =User.objects.create_user(username=username, email=email,password=password)
                user.save()  
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request,user_login)
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('account:profile')
        else:
            messages.info(request,'Password mismatch')  
            return redirect('account:signup')
    else:
        return render(request,'registration/signup.html')
   


def signin(request):
    if request.method == 'POST':
        username=request.POST['username'] 
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)   
            return redirect('/') 
        else:
            messages.info(request,'credentials invalid')  
            return redirect('account:signin')
    else:
        return render(request,'registration/signin.html') 


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('account:signin')







