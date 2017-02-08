from django.shortcuts import render
from collection.models import Thing
# Create your views here.

def index(request):
    # Dynamic variable yay :3
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'things': things,
        })
