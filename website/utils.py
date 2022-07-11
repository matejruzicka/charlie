import enum

from website.models import BoardMember


class FileTypes(enum.Enum):
    pdf = "application/pdf"
    doc = "application/msword"
    docx = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    jpg = "image/jpeg"
    jpeg = "image/jpeg"
    png = "image/png"


def sort_members():
    president = BoardMember.objects.filter(title="Prezident")
    vicepresident = BoardMember.objects.filter(title="Víceprezident")
    secretary = BoardMember.objects.filter(title="Tajemník")
    treasurer = BoardMember.objects.filter(title="Pokladník")
    board_member = BoardMember.objects.filter(title="Řadový člen")
    audit_comittee_member = BoardMember.objects.filter(title="Člen revizní komise")

    board_members = []
    if president:
        board_members.append(president[0])
    if vicepresident:
        board_members.append(vicepresident[0])
    if secretary:
        board_members.append(secretary[0])
    if treasurer:
        board_members.append(treasurer[0])
    if board_member:
        for member in board_member:
            board_members.append(member)
    if audit_comittee_member:
        for member in audit_comittee_member:
            board_members.append(member)

    return board_members


if __name__ == "__main__":
    pass
