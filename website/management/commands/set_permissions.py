from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'help'

    def handle(self, *args, **options):
        try:
            perm_full = Permission(content_type=ContentType.objects.get(app_label="website", model="member"),
                                   name="Full access", codename="full_access")
            perm_full.save()
            perm_restricted = Permission(content_type=ContentType.objects.get(app_label="website", model="member"),
                                         name="Restricted access", codename="restricted_access")
            perm_restricted.save()
        except:
            perm_full = Permission.objects.get(codename="full_access")
            perm_restricted = Permission.objects.get(codename="restricted_access")

        try:
            admin = User(username="admin", password="spolekcharlie", is_staff=True, is_active=True, is_superuser=True)
            admin.save()
        except:
            admin = User.objects.get(username="admin")
        admin.user_permissions.add(perm_full)
        admin.save()

        prezident = User(username="prezident", password="spolekcharlie", is_staff=True, is_active=True,
                         is_superuser=False)
        prezident.save()
        prezident.user_permissions.add(perm_full,
                                       Permission.objects.get(codename="view_university"),
                                       Permission.objects.get(codename="delete_university"),
                                       Permission.objects.get(codename="change_university"),
                                       Permission.objects.get(codename="add_university"),
                                       Permission.objects.get(codename="view_photo"),
                                       Permission.objects.get(codename="delete_photo"),
                                       Permission.objects.get(codename="change_photo"),
                                       Permission.objects.get(codename="add_photo"),
                                       Permission.objects.get(codename="view_member"),
                                       Permission.objects.get(codename="delete_member"),
                                       Permission.objects.get(codename="change_member"),
                                       Permission.objects.get(codename="add_member"),
                                       Permission.objects.get(codename="view_file"),
                                       Permission.objects.get(codename="delete_file"),
                                       Permission.objects.get(codename="change_file"),
                                       Permission.objects.get(codename="add_file"),
                                       Permission.objects.get(codename="view_faculty"),
                                       Permission.objects.get(codename="delete_faculty"),
                                       Permission.objects.get(codename="change_faculty"),
                                       Permission.objects.get(codename="add_faculty"),
                                       Permission.objects.get(codename="view_boardmember"),
                                       Permission.objects.get(codename="delete_boardmember"),
                                       Permission.objects.get(codename="change_boardmember"),
                                       Permission.objects.get(codename="add_boardmember"),
                                       Permission.objects.get(codename="view_logentry"),
                                       )
        prezident.save()

        viceprezident = User(username="viceprezident", password="spolekcharlie", is_staff=True, is_active=True,
                             is_superuser=False)
        viceprezident.save()
        viceprezident.user_permissions.add(Permission.objects.get(codename="view_photo"),
                                           Permission.objects.get(codename="delete_photo"),
                                           Permission.objects.get(codename="change_photo"),
                                           Permission.objects.get(codename="add_photo"),
                                           Permission.objects.get(codename="view_file"),
                                           Permission.objects.get(codename="delete_file"),
                                           Permission.objects.get(codename="change_file"),
                                           Permission.objects.get(codename="add_file"),
                                           Permission.objects.get(codename="view_boardmember"),
                                           Permission.objects.get(codename="delete_boardmember"),
                                           Permission.objects.get(codename="change_boardmember"),
                                           Permission.objects.get(codename="add_boardmember"),
                                           )
        viceprezident.save()

        tajemnik = User(username="tajemnik", password="spolekcharlie", is_staff=True, is_active=True,
                        is_superuser=False)
        tajemnik.save()
        tajemnik.user_permissions.add(perm_full, Permission.objects.get(codename="view_photo"),
                                      Permission.objects.get(codename="delete_photo"),
                                      Permission.objects.get(codename="change_photo"),
                                      Permission.objects.get(codename="add_photo"),
                                      Permission.objects.get(codename="view_member"),
                                      Permission.objects.get(codename="delete_member"),
                                      Permission.objects.get(codename="change_member"),
                                      Permission.objects.get(codename="add_member"),
                                      Permission.objects.get(codename="view_file"),
                                      Permission.objects.get(codename="delete_file"),
                                      Permission.objects.get(codename="change_file"),
                                      Permission.objects.get(codename="add_file"),
                                      Permission.objects.get(codename="view_university"),
                                      Permission.objects.get(codename="delete_university"),
                                      Permission.objects.get(codename="change_university"),
                                      Permission.objects.get(codename="add_university"),
                                      Permission.objects.get(codename="view_faculty"),
                                      Permission.objects.get(codename="delete_faculty"),
                                      Permission.objects.get(codename="change_faculty"),
                                      Permission.objects.get(codename="add_faculty"),
                                      Permission.objects.get(codename="view_boardmember"),
                                      Permission.objects.get(codename="delete_boardmember"),
                                      Permission.objects.get(codename="change_boardmember"),
                                      Permission.objects.get(codename="add_boardmember"),
                                      Permission.objects.get(codename="view_logentry"),
                                      )
        tajemnik.save()

        pokladnik = User(username="pokladnik", password="spolekcharlie", is_staff=True, is_active=True,
                         is_superuser=False)
        pokladnik.save()
        pokladnik.user_permissions.add(perm_restricted, Permission.objects.get(codename="view_photo"),
                                       Permission.objects.get(codename="delete_photo"),
                                       Permission.objects.get(codename="change_photo"),
                                       Permission.objects.get(codename="add_photo"),
                                       Permission.objects.get(codename="view_member"),
                                       Permission.objects.get(codename="change_member"),
                                       Permission.objects.get(codename="view_file"),
                                       Permission.objects.get(codename="delete_file"),
                                       Permission.objects.get(codename="change_file"),
                                       Permission.objects.get(codename="add_file"),
                                       Permission.objects.get(codename="view_boardmember"),
                                       Permission.objects.get(codename="delete_boardmember"),
                                       Permission.objects.get(codename="change_boardmember"),
                                       Permission.objects.get(codename="add_boardmember"),
                                       Permission.objects.get(codename="view_logentry"),
                                       )
        pokladnik.save()

        radovy_clen = User(username="radovy_clen", password="spolekcharlie", is_staff=True, is_active=True,
                           is_superuser=False)
        radovy_clen.save()
        radovy_clen.user_permissions.add(Permission.objects.get(codename="view_photo"),
                                         Permission.objects.get(codename="delete_photo"),
                                         Permission.objects.get(codename="change_photo"),
                                         Permission.objects.get(codename="add_photo"),
                                         Permission.objects.get(codename="view_file"),
                                         Permission.objects.get(codename="delete_file"),
                                         Permission.objects.get(codename="change_file"),
                                         Permission.objects.get(codename="add_file"),
                                         Permission.objects.get(codename="view_boardmember"),
                                         Permission.objects.get(codename="delete_boardmember"),
                                         Permission.objects.get(codename="change_boardmember"),
                                         Permission.objects.get(codename="add_boardmember"),
                                         )
        radovy_clen.save()
