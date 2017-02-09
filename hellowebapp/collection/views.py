from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing


# Create your views here.

def index(request):
    # Dynamic variable yay :3
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'things': things,
    })


def thing_detail(request, slug):

    thing = Thing.objects.get(slug=slug)

    return render(request, 'things/thing_detail.html', {
        'thing': thing
        })


def edit_thing(request, slug):
    #Taking object
    thing = Thing.objects.get(slug=slug)

    #Magic
    form_class = ThingForm

    if request.method == 'POST':

        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    else:
        #What is this form class magic
        form = form_class(instance=thing)

    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,})

