from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from website.models import Member


class Command(BaseCommand):
    help = "This command does this and that"

    def handle(self, *args, **options):
        # member = Member.objects.create(first_name="Jaromir", last_name="Nuzek", membership_type="Roční",
        #                                paid_membership=True, member_since=(datetime.now() - timedelta(days=340)),
        #                                photos_allowed=True, approved=True, found_application=True,
        #                                ending_membership=False,
        #                                membership_last_prolonged=(datetime.now() - timedelta(days=340)))
        # member.save()

        ending_filter = Member.objects.filter(
            membership_type="Roční",
            paid_membership=True,
            membership_last_prolonged__lte=(datetime.now().date() - timedelta(days=335))
        )

        for member in ending_filter:
            member.ending_membership = True
            member.save()

        ended_filter = Member.objects.filter(
            membership_type="Roční",
            paid_membership=True,
            membership_last_prolonged__lte=(datetime.now().date() - timedelta(days=365))
        )

        for member in ended_filter:
            member.paid_membership = False
            member.save()