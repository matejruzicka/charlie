from django.contrib import admin

from website import models

admin.site.register(models.BoardMember)
admin.site.register(models.File)
admin.site.register(models.Photo)
