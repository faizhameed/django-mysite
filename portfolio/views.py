from django.http import HttpResponse
from django.template import loader

from .models import Experience


def index(request):
    explist = Experience.objects.all()
    template = loader.get_template('portfolio/index.html')
    context = {
        'explist': explist
    }
    return HttpResponse(template.render(context, request))