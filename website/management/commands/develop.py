from django.core.management.base import BaseCommand

from website.models import BoardMember


class Command(BaseCommand):
    help = "This command does this and that"

    def handle(self, *args, **options):
        kuba = BoardMember(name="Jakub Šváb", title="Prezident", pronouns="Mužské")
        kuba.save()
