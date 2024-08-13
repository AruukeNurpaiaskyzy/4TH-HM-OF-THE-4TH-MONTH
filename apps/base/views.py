from django.shortcuts import render
from apps.base.models import Index, About, Action, Image
# Create your views here.

def index(request):
    index = Index.objects.latest('id')
    about = About.objects.all().order_by('?')[:3]
    action = Action.objects.all()
    image_id = Image.objects.latest('id')
    return render(request, "index.html", locals())

