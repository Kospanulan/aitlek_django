from django.contrib import admin

from blog import models

admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Tag)
