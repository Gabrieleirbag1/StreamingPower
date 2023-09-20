from .forms import IdeForm

def ide_form_context(request):
    form = IdeForm(request.POST or None)
    return {'ide_form': form}
