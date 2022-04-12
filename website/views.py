from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from website.models import BoardMember, File
from website.utils import FileTypes


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def downloads(request):
    files = File.objects.all()
    return render(request, "downloads.html", {"files": files})


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


def board(request):
    board_members = BoardMember.objects.all()
    return render(request, "board.html", {"board_members": board_members})

