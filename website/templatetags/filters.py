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


@register.filter(name='mobile_filter')
def mobile_filter(ahoj):
    return "pl-5"
