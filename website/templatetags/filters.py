import math

from django import template

register = template.Library()


@register.filter(name='path_filter')
def path_filter(path):
    path = "Spolek Charlie" + path.replace("/", " | ")[:-2]
    return path


@register.filter(name='board_title_filter')
def board_title_filter(member):
    if member.pronouns == "Mužské":
        return member.title
    else:
        if "rezident" in member.title:
            return member.title + "ka"
        elif member.title == "Tajemník":
            return "Tajemnice"
        elif member.title == "Řadový člen":
            return "Řadová členka"
        elif member.title == "Člen revizní komise":
            return "Členka revizní komise"


@register.filter(name="static")
def static(path):
    return path.split("/charlie/")[1]


@register.filter(name="photos")
def photos(photos, number):
    print([photo.description for photo in photos])
    third = int((len(photos)/3))
    if number == 1:
        print([photo.description for photo in list(photos)[:1]])
        return list(photos)[:third]
    elif number == 2:
        print([photo.description for photo in list(photos[1:3])])
        return list(photos)[third:(third*2)]
    else:
        print([photo.description for photo in list(photos[3:])])
        return list(photos)[(third*2):]

