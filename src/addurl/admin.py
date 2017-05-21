# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from addurl.models import Link


class BookmarkAdmin(admin.ModelAdmin):

    list_display = ['__unicode__','created']
    class Meta:
        model = Link


admin.site.register(Link,BookmarkAdmin)