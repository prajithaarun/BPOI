from pyexpat.errors import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse
from django.conf import settings
from werkzeug.utils import redirect
from .form import SubscribeForm

def hr(request):
    return HttpResponse("Email Send Successfully")

def subscribe(request):
    if request.method=='GET':
        form=SubscribeForm()
        return render(request, 'email.html', {'form': form})
    else:
        form = SubscribeForm(request.POST)
        if form.is_valid():
            #subject = 'Mail from Prajitha'
            message = " Welcome To Athena Erudition"
            subject=form.cleaned_data.get('subject')
            # message=form.cleaned_data.get('message')
            recipient=form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient],fail_silently=False)
            form = SubscribeForm()
            return render(request, 'email.html', {'form': form})
