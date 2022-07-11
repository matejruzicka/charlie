from django import template

register = template.Library()


@register.filter(name='path_filter')
def path_filter(path):
    path = "Spolek Charlie" + path.replace("/", " | ")[:-2]
    return path


@register.filter(name='board_title_filter_en')
def board_title_filter_en(member):
    if "Prezident" in member.title:
        return "President"
    elif "rezident" in member.title:
        return "Vicepresident"
    elif member.title == "Tajemník":
        return "Secretary"
    elif member.title == "Řadový člen":
        return "Rank Member"
    elif member.title == "Člen revizní komise":
        return "Member of the Audit Committee"
    elif member.title == "Pokladník":
        return "Treasurer"


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

