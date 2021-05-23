from django.shortcuts import render,redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def all_shows(request):
    context = {
        "all_shows" : Show.objects.all(),
    }
    return render(request, 'all_shows.html', context)

def one_show(request, show_id):
    context = {
        "show" : Show.objects.get(id=show_id)
    }
    return render(request,'one_show.html',context)

def create(request):
    if request.method == "GET":
        return render(request,'new_show.html')
    else:
        new_title = request.POST['title']
        network = request.POST['network']
        new_date = request.POST['date']
        new_desc = request.POST['desc']
        new_network = Network.objects.create(name=network)

        Show.objects.create(title=new_title, network=new_network, release_date=new_date, desc=new_desc)
        return redirect('/')

def edit(request, show_id):
    show = Show.objects.get(id=show_id)
    if request.method == "GET":
        context = {
            "show" : show,
        }
        return render(request,'edit.html',context)
    else:
        title = request.POST['title']
        network = request.POST['network']
        date = request.POST['date']
        desc = request.POST['desc']

        show.title = title
        show.network.name = network
        show.release_date = date
        show.desc = desc
        show.save()
        return redirect(f'/shows/{show.id}')

def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')
