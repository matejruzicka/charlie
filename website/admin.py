from django.contrib import admin

from website import models


class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["first_name", "last_name"]}),
        ("Kontaktní informace", {"fields": ["email", "phone"]}),
        ("Univerzita", {"fields": ["university", "faculty"]}),
        ("Členství", {"fields": ["membership_type", "paid_membership", "member_since", "member_until",
                                 "membership_last_prolonged", "lifetime_since", "approved", "found_application"]}),
        (None, {"fields": ["photos_allowed"]}),
    ]

    list_display = ("last_name", "first_name", "membership_type", "member_since", "member_until",
                    "paid_membership", "approved", "ending_membership")

    list_filter = ["member_since", "university", "faculty", "membership_type", "approved", "found_application", "ending_membership"]


admin.site.register(models.BoardMember)
admin.site.register(models.File)
admin.site.register(models.Photo)
admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.University)
admin.site.register(models.Faculty)
