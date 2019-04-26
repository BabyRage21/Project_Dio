from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from django.utils.timezone import utc

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.messages import constants as messages
from django.contrib.auth.forms import UserCreationForm
from userApp.forms import *



def registration(request):
    if request.method == 'POST':
        form1=ProfileForm
        userform=UserForm
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'userApp/reg.html', {'form': form1})
        else:
            #TEMP
            return HttpResponse('WRONG!!!')
            #return render(request, 'userApp/reg.html', {'form': form1})
    else:
        form = UserCreationForm()
        return render(request, 'userApp/create_user.html', {'form': form})


@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        musician_form = MusicianProfile(request.POST, instance=request.user.profile)
        company_form = CompanyProfile(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            #return redirect('settings:profile')
            return HttpResponse('success blyatj!')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        musician_form=MusicianForm(instance=request.user.profile)
        company_form = CompanyForm(instance=request.user.profile)
    #TEMP
    return render(request, 'userApp/reg.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'musician_form': musician_form,
        'company_form': company_form,
    })



def feed(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


def allpersons(request):
    persons = Person.objects
    return render(request, 'userApp/allpersons.html', {'persons':persons})
 
def detail(request, person_id):
    persondetail = get_object_or_404(Person, pk=person_id)
    return render(request, 'userApp/detail.html', {'person':persondetail})


'''
def registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        #registertime = request.POST.get("registertime")
        date = request.POST.get("date")
        password = request.POST.get("password")
        spec = request.POST.get("spec")
        image= request.POST.get("image")
        p = Person()
        p.name=name
        p.registertime=datetime.datetime.utcnow().replace(tzinfo=utc)
        p.date=date
        p.spec=spec
        p.phone=1337
        p.description='description'
        p.email='nu da'
        p.clean()
        p.image=image

        p.save()
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        personform = PersonForm()
        return render(request, "userApp/reg.html", {"form": personform})

def login(request):
    pass
'''