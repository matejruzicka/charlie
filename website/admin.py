from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Permission

from website import models


# TODO: moznost vsech useru readonly members nektere pole - probrat na vyboru

class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ["ending_membership"]

    def get_readonly_fields(self, request, obj=None):
        if request.user.has_perm("website.full_access"):
            return ["ending_membership"]
        elif request.user.has_perm("website.restricted_access"):
            return ["first_name", "last_name", "email", "phone", "member_since",
                    "university", "faculty", "ending_membership", "approved", "found_application", "photos_allowed"]
        else:
            return super(admin.ModelAdmin, self).get_readonly_fields(request, obj)

    def changelist_view(self, request, extra_context=None):
        if request.user.has_perm("website.full_access"):
            self.fieldsets = [
                ("Kontaktní informace", {"fields": ["email", "phone"]}),
                ("Univerzita", {"fields": ["university", "faculty"]}),
                ("Členství", {"fields": ["membership_type", "paid_membership", "member_since", "member_until",
                                         "membership_last_prolonged", "lifetime_since", "approved",
                                         "found_application"]}),
                (None, {"fields": ["photos_allowed"]}),
            ]
            self.list_display = ("last_name", "first_name", "membership_type", "member_since", "member_until",
                                 "paid_membership", "approved", "ending_membership")
            self.list_filter = ["member_since", "university", "faculty", "membership_type", "approved",
                                "found_application", "ending_membership"]
            self.search_fields = ["last_name", "faculty__name"]

        elif request.user.has_perm("website.restricted_access"):
            self.fieldsets = [
                ("Kontaktní informace", {"fields": ["email", "phone"]}),
                ("Univerzita", {"fields": ["university", "faculty"]}),
                ("Členství", {"fields": ["membership_type", "paid_membership", "member_since", "member_until",
                                         "membership_last_prolonged", "lifetime_since", "approved",
                                         "found_application"]}),
                (None, {"fields": ["photos_allowed"]}),
            ]
            self.list_display = ("first_name", "last_name", "membership_type", "member_since", "member_until",
                                 "paid_membership", "ending_membership")
            self.list_filter = ["membership_type", "paid_membership", "ending_membership"]
            self.editable = ["membership_type", "membership_last_prolonged", "paid_membership",
                             "lifetime_since"]
        else:
            self.list_display = ()
        return super(MemberAdmin, self).changelist_view(request, extra_context)

    def get_form(self, request, obj=None, **kwargs):
        if request.user.has_perm("website.full_access"):
            self.fields = ["last_name", "first_name", "email", "phone", "membership_type", "member_since", "member_until",
                           "paid_membership", "approved", "email", "phone"]
        elif request.user.has_perm("website.restricted_access"):
            self.fields = ["membership_type", "paid_membership", "member_since",
                           "membership_last_prolonged", "lifetime_since", "ending_membership", "approved", "email",
                           "phone", "university", "faculty", "photos_allowed", "found_application"]
            self.list_filter = ["membership_type", "ending_membership", "paid_membership", "membership_last_prolonged",
                                "lifetime_since"]
        else:
            self.fields = []
        return super(MemberAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(models.BoardMember)
admin.site.register(models.File)
admin.site.register(models.Photo)
admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.University)
admin.site.register(models.Faculty)
admin.site.register(Permission)
admin.site.register(LogEntry)
