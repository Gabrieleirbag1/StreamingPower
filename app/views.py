from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import IdeForm, ImgForm, InsForm, SigForm
from . import models
from propterre.models import Ide, Img
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views import View
import os
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings  
import requests
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


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
    if request.user.is_authenticated:
        return redirect(home)
    else:
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
                
                image_url = 'http://films.lizziewizzie.site/films_et_series/ne-pas-supprimer-profil.jpg'
                response = requests.get(image_url)
                
                if response.status_code == 200:

                    img = Img(nom=username, imgid=user)
                    img.save()
                    
                    # Créez un objet ContentFile à partir du contenu téléchargé
                    content_file = ContentFile(response.content)
                    
                    # Associez le contenu au champ 'fichier' de l'objet Img
                    img.fichier.save(f'Photo-de-profil-{username}.jpg', content_file, save=True)
                
                return redirect(register)
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        Ide = models.Ide.objects.order_by('-id')
        Ins = models.Ins.objects.order_by('-id')
        Sig = models.Sig.objects.order_by('-id')
        user_list = User.objects.order_by('-id')
        return render(request, 'propterre/adminpage.html', {'Ide_charge': Ide, 'user_charge': user_list, 'Ins_charge': Ins, 'Sig_charge': Sig})



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
    

@login_required(login_url='/login_user')
def profil(request, id):
    img = Img.objects.get(pk=id)

    if request.method == 'POST':
        lform = ImgForm(request.POST, request.FILES, instance=img)
        if lform.is_valid():
            user_to_delete = User.objects.get(username=request.user.username)
            img_to_delete = Img.objects.filter(imgid=user_to_delete).first()
            
            if img_to_delete:
                file_path = os.path.join(settings.MEDIA_ROOT, str(img_to_delete.fichier))
                if os.path.exists(file_path):
                    os.remove(file_path)
                img_to_delete.delete()

            lform.save()
            referer = request.META.get('HTTP_REFERER', "/")
        return redirect(referer)
    else:
        lform = ImgForm(instance=img)
    
    return render(request, "propterre/profil.html", {"form": lform, "id": id})

        

@user_passes_test(lambda user: user.is_superuser, login_url='/propterre/home')
def delete(request, id):
    ide = models.Ide.objects.get(id=id)
    ide.delete()
    return redirect(register)



@user_passes_test(lambda user: user.is_superuser, login_url='/propterre/home')
def deleteuser(request, username):
    try:
        user_to_delete = User.objects.get(username=username)

        try:
            img_to_delete = Img.objects.get(imgid=user_to_delete)
            file_path = os.path.join(settings.MEDIA_ROOT, str(img_to_delete.fichier))
 
            if os.path.exists(file_path):
                os.remove(file_path)
            
            img_to_delete.delete()
        except ObjectDoesNotExist:
            pass

        user_to_delete.delete()
        
        return redirect(register)
    except User.DoesNotExist:
        messages.error(request, 'User not found')
        return redirect(register)



''' ---------------------------------------------------------------MEDIA --------------------------------------------------------------------'''

class Download(View):
    template_name = 'propterre/affiche.html'

    def get(self, request):
        form = ImgForm()
        objets = Img.objects.all()
        return render(request, self.template_name, {'form': form, 'objets': objets})

    def post(self, request, id=None):
        #méthode delete
        if id is not None:
            try:
                objet = Img.objects.get(pk=id)
                objet.delete()
                return redirect(home)
            except Img.DoesNotExist:
                return HttpResponseNotFound("L'objet que vous essayez de supprimer n'existe pas.")

        form = ImgForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(home)

        objets = Img.objects.all()
        return render(request, self.template_name, {'form': form, 'objets': objets})
    

#_________________________________SIGNALEMENT ET AJOUT DE COMPTE_________________________#

def ajoutins(request):
    form = InsForm(request.POST or None) 
    if request.method == "POST":
        if form.is_valid():
            ins = form.save()
            pass
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass


def traitementins(request):
    if request.method == 'POST':
        lform = InsForm(request.POST)
        if lform.is_valid():
            ins = lform.save()
            referer = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(f"{referer}#error-section")
        else:
            messages.info(request, "Le formulaire n'est pas valide. Veuillez corriger les erreurs.")
            referer = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(f"{referer}#error-section")
    else:
        referer = request.META.get('HTTP_REFERER', "/")
        return redirect(referer)
    
@user_passes_test(lambda user: user.is_superuser, login_url='/propterre/home')
def deleteins(request, id):
    ins = models.Ins.objects.get(id=id)
    ins.delete()
    return redirect(register)
    


def ajoutsig(request):
    form = SigForm(request.POST or None) 
    if request.method == "POST":
        if form.is_valid():
            sig = form.save()
            pass
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    pass


def traitementsig(request):
    if request.method == 'POST':
        lform = SigForm(request.POST)
        if lform.is_valid():
            sig = lform.save()
            referer = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(f"{referer}#error-section")
        else:
            messages.info(request, "Le formulaire n'est pas valide. Veuillez corriger les erreurs.")
            referer = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(f"{referer}#error-section")
    else:
        referer = request.META.get('HTTP_REFERER', "/")
        return redirect(referer)
    
@user_passes_test(lambda user: user.is_superuser, login_url='/propterre/home')
def deletesig(request, id):
    sig = models.Sig.objects.get(id=id)
    sig.delete()
    return redirect(register)


    
    






