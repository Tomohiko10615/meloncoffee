# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

# Subscription Logic
def subscribe(first_name, second_name, phone, birthday, email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "pending",
        'merge_fields': {
            'FNAME': first_name,
            'LNAME': second_name,
        }
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))

"""
def showform(request):
    form= FormContactForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'registration/signup.html', context)
"""


def signup(request):
    form = CustomUserCreationForm(request.POST)
    print(form.errors)
    if request.method == "POST":
        
        if form.is_valid():
            first_name = request.POST['first_name']
            second_name = request.POST['second_name']
            phone = request.POST['phone']
            birthday = request.POST['birthday']
            email = request.POST['email']
            subscribe(first_name, second_name, phone, birthday, email) 
            messages.success(request, "Email received. thank You! ") # message
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            return render(request, "registration/signup.html", {
        'form': form, 'failed': True})

    return render(request, "registration/signup.html", {
        'form': form,})
    

def login(request):
    return render(request, "registration/login.html")

def sample(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            first_name = request.POST['first_name']
            second_name = request.POST['second_name']
            phone = request.POST['phone']
            birthday = request.POST['birthday']
            email = request.POST['email']
            subscribe(first_name, second_name, phone, birthday, email) 
            messages.success(request, "Email received. thank You! ") # message
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))

    return render(request, "registration/sample.html", {
        'form': form,})

"""
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Sample(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sample.html'
"""