from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.urls import reverse

from user.form import CustomUserCreationForm


def home(request):
    return HttpResponse("HOME PAGE")
def register_view(request):
    form=CustomUserCreationForm()
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('register'))
    return render(request,'registration/register.html',{'form':form})
