from django.core.management.base import BaseCommand
from website.models import Member


class Command(BaseCommand):
    help = 'help'

    def handle(self, *args, **options):
        members = Member.objects.all()
        for member in members:
            member.delete()
