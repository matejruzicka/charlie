import itertools

from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from website.models import File, Photo
from website.utils import FileTypes, sort_members


def home(request):
    board_members = sort_members()
    files = File.objects.filter(slug__in=["prihlaska", "stanovy", "jednaci-rad-vh", "volebni-rad-vh"])
    return render(request, "home.html", {"board_members": board_members, "files": files})


def about(request):
    return render(request, "about.html")


def gallery(request):
    photos = Photo.objects.all()
    wide = []
    high = []

    for image in photos:
        width, height = image.photo.width, image.photo.height
        if width > height:
            wide.append(image)
        else:
            high.append(image)

    photos = [x for x in itertools.chain.from_iterable(itertools.zip_longest(wide, high)) if x]

    return render(request, "gallery.html", {"photos": photos})


def upcoming_events(request):
    return render(request, "upcoming_events.html")


def magazine(request):
    file = get_object_or_404(File, slug="magazine")
    response = HttpResponse(file.file)
    response["Content-Type"] = FileTypes[file.file_type].value
    response["Content-Disposition"] = f"inline; filename={file.name}.{file.file_type}"
    return response


def download_file(request, slug):
    file = get_object_or_404(File, slug=slug)
    response = HttpResponse(file.file)
    response["Content-Type"] = FileTypes[file.file_type].value
    response["Content-Disposition"] = f"attachment; filename={file.name}.{file.file_type}"
    return response


def view_file(request, slug):
    file = get_object_or_404(File, slug=slug)
    response = HttpResponse(file.file)
    response["Content-Type"] = FileTypes[file.file_type].value
    response["Content-Disposition"] = f"inline; filename={file.name}.{file.file_type}"
    return response

