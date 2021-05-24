from django.shortcuts import render,redirect
from django.contrib import messages
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
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
        else:
            new_title = request.POST['title']
            network = request.POST['network']
            new_date = request.POST['date']
            new_desc = request.POST['desc']
            new_network = Network.objects.create(name=network)

            Show.objects.create(title=new_title, network=new_network, release_date=new_date, desc=new_desc)
            messages.success(request, "Show Creation Successful!")
            return redirect('/')

def edit(request, show_id):
    show = Show.objects.get(id=show_id)
    if request.method == "GET":
        context = {
            "show" : show,
        }
        return render(request,'edit.html',context)
    else:
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
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
            messages.success(request, "Show successfully updated!")
            return redirect(f'/shows/{show.id}')

def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')
