from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

# Home page will be using our home.html template from the templates folder.  Our urls.py file will be referencing the below view for our home page


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password does not exist')

    context = {}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        # in Django, the double underscore is used in query expressions to access related fields or to apply specific query transformations such as lookups
        Q(topic__name__icontains=q) |
        # the vertical line between each of the Q objects here represents OR
        Q(name__icontains=q) |
        # icontains: Case-insensitive containment test
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
