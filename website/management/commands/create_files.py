from django.core.management.base import BaseCommand

from website.models import File


class Command(BaseCommand):
    help = "This command does this and that"

    def handle(self, *args, **options):
        File.objects.all().delete()

        prihlaska = File(name="Přihláška", slug="prihlaska", file_type="pdf",
                       file="charlie/static/prihlaska.pdf")
        prihlaska.save()

        stanovy = File(name="Stanovy", slug="stanovy", file_type="pdf",
                       file="charlie/static/stanovy.pdf")
        stanovy.save()

        casopis = File(name="Časopis", slug="magazine", file_type="pdf",
                       file="charlie/static/Charlie_magazin_jaro_2022.pdf")
        casopis.save()
