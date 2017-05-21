# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.


class Link(models.Model):

    title = models.CharField(max_length=220)
    url = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def link_delete_url(self):
    	return reverse("bookmarks:delete_url", kwargs = {"id":self.id})

    def link_update_url(self):
    	return reverse("bookmarks:update_url", kwargs = {"id":self.id})