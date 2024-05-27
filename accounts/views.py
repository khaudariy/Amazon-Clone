from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import SignUpForm,UserActivationForm,UserCreationForm
from .models import Profile
# Create your views here.


def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email = form.cleaned_data['email']

            user = form.save(commit=False)
            user.is_active = False

            form.save()
            profile = Profile.objects.get(user__username=username)
            send_mail(
                "Activate your Account",
                f"Welcome {username} \n Use this code {profile.code} to activate your account ",
                "hossamkhaudariy0@gmail.com",
                [email],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')

    else:
        form = SignUpForm()
    return render(request,'accounts/signup.html',{'form':form})        



def user_activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method=='POST':
        form = UserActivationForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code == profile.code:
                profile.code=''
                user=User.objects.get(username=username)
                user.is_active=True
                user.save()
                profile.save
                return redirect('/accounts/login')
    else:
        form=UserActivationForm()
    return render (request,'accounts/activate.html',{'form':form})        
