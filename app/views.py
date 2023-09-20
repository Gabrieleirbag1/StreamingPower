from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import IdeForm
from . import models
from propterre.models import Ide
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.

@login_required(login_url='/login_user')
def films(request):
    return render(request, 'propterre/films.html')

@login_required(login_url='/login_user')
def series(request):
    return render(request, 'propterre/series.html')

@login_required(login_url='/login_user')
def head(request):
    return render(request, 'propterre/head.html')

@login_required(login_url='/login_user')
def home(request):
    return render(request, 'propterre/home.html')


def affiche(request):
    return render(request, 'propterre/affiche.html')



def nothome(request):
    return render(request, 'propterre/nothome.html')

@user_passes_test(lambda user: user.is_superuser, login_url='/propterre/home')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                
                return redirect(register)
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        Ide = models.Ide.objects.order_by('-id')
        user_list = User.objects.order_by('-id')
        return render(request, 'propterre/adminpage.html', {'Ide_charge': Ide, 'user_charge': user_list})



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # check if user is "admin"
            if user.is_superuser:
                auth.login(request, user)
                return redirect(register)
            
            else:
                auth.login(request, user)
                return redirect(home)
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect(login_user)

    else:
        return render(request, 'propterre/login.html')



def logout_user(request):
    auth.logout(request)
    return redirect(nothome)


def ajout(request):
    form = IdeForm(request.POST or None) 
    if request.method == "POST":
        if form.is_valid():
            ide = form.save()
            pass
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass


def traitement(request):
    if request.method == 'POST':
        lform = IdeForm(request.POST)
        if lform.is_valid():
            ide = lform.save()
            referer = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(f"{referer}#error-section")
        else:
            messages.info(request, "Le formulaire n'est pas valide. Veuillez corriger les erreurs. (10 et 30 caractères maximum)")
            referer = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(f"{referer}#error-section")
    else:
        referer = request.META.get('HTTP_REFERER', "/")
        return redirect(referer)

    
def update(request, id):
    ide = models.Ide.objects.get(pk = id)
    lform = IdeForm(request.POST)
    if lform.is_valid():
        ide = lform.save(commit=False) 
        ide.id = id; 
        ide.save() 
        return HttpResponseRedirect('/propterre/')
    else:
        ide = models.Ide.objects.get(pk = id)
        lform = IdeForm(instance=ide)
        return render(request, "propterre/update.html", {"form": lform, "id": id})
    

@user_passes_test(lambda user: user.is_superuser, login_url='/propterre/home')
def delete(request, id):
    ide = models.Ide.objects.get(id=id)
    ide.delete()
    return redirect(register)

@user_passes_test(lambda user: user.is_superuser, login_url='/propterre/home')
def deleteuser(request, username):
    user_to_delete = User.objects.get(username=username)
    user_to_delete.delete()
    return redirect(register)

