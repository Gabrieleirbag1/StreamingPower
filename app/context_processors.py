from .forms import IdeForm

def ide_form_context(request):
    form = IdeForm(request.POST or None)
    return {'ide_form': form}


#me permet de mettre le formulaire dans le footer de toutes les pages
