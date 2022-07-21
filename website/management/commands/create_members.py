import json
from datetime import datetime

from django.core.management.base import BaseCommand
from website.models import Member, University, Faculty


with open("path/to/members.json", "r") as fle:
    members: dict = json.loads(fle.read())


class Command(BaseCommand):
    help = 'Creates members in db from json file'

    def handle(self, *args, **options):
        for member in members:
            obj = Member.objects.create(first_name=member.get("first_name"), last_name=member.get("last_name"),
                                        email=member.get("email"), phone=member.get("phone"),
                                        photos_allowed=member.get("photos_allowed", False),
                                        paid_membership=member.get("paid_application", False),
                                        approved=member.get("approved", False),
                                        found_application=member.get("found_application", False),
                                        membership_type=("Doživotní" if member.get("lifelong_membership") else "Roční"),
                                        ending_membership=False,
                                        )

            if member.get("last_prolonged"):
                obj.membership_last_prolonged = datetime.strptime(member.get("last_prolonged"), "%#d. %#m. %Y")

            if member.get("member_since"):
                obj.member_since = datetime.strptime(member.get("member_since"), "%#d. %#m. %Y")

            if member.get("member_until"):
                obj.member_until = datetime.strptime(member.get("member_until"), "%#d. %#m. %Y")

            if member.get("lifetime_since"):
                obj.lifetime_since = datetime.strptime(member.get("lifetime_since"), "%#d. %#m. %Y")

            if University.objects.filter(name=member.get("university")):
                obj.university = University.objects.get(name=member.get("university"))

            if Faculty.objects.filter(name=member.get("faculty")):
                obj.faculty = Faculty.objects.get(name=member.get("faculty"))

            obj.save()
