from django.shortcuts import render

from website.models import BoardMember, File, Photo
from website.utils import sort_members


def home_en(request):
    board_members = sort_members()
    files = File.objects.filter(slug__in=["prihlaska", "stanovy", "jednaci-rad-vh", "volebni-rad-vh"])
    return render(request, "home_en.html", {"board_members": board_members, "files": files})


def about_en(request):
    return render(request, "about_en.html")


def gallery_en(request):
    photos = Photo.objects.all()
    return render(request, "gallery_en.html", {"photos": photos})


def upcoming_events_en(request):
    return render(request, "upcoming_events_en.html")


