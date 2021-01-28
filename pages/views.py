from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import SubmitForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import (PermissionRequiredMixin)

# from django.core.mail import send_mail




# Create your views here.

def home(request):
   return render(request, 'home.html')
# @permission_required('about')
# def about(request):
#    return render(request, 'about.html', permission_required = 'about')

class AboutPageView(PermissionRequiredMixin,TemplateView):
    template_name="about.html"
    permission_required = 'pages.about'

def password_reset_form(request):
   return render(request, 'password_reset_form.html')



def fill (request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required	

            email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            address1 = form.cleaned_data['address1']
            address2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']

            
            form.save()

            
            return HttpResponseRedirect("/thanks")
            # return render(request, 'thanks.html')
            # ...
            # redirect to a new URL:
            
    # if a GET (or any other method) we'll create a blank form
    else:

        form = SubmitForm()

    return render(request, 'form.html', {'form': form})


def thanks(request):
   return render(request, 'thanks.html')

    



