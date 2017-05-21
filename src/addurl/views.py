# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
# Create your views here.
from addurl.models import Link
from addurl.forms import URLform
from addurl.utils import get_page_title


def link_list(request):
    # queryset=Link.objects.all()
    form = URLform(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        url = form.cleaned_data.get('url')
        instance.title = get_page_title(url)
        instance.save()
        return redirect("bookmarks:data")
    return render(request, "base.html")


def link_data(request):
    form = URLform(request.POST or None)
    queryset = Link.objects.all()

    context = {
        "url": queryset,
        "form":form
    }
    return render(request, "base.html", context)

# def link_update(requests,id):
#     instance = get_object_or_404(Link,id=id,instance=instance)
#     form = get_object_or_404

def link_delete(request,id=None):
    instance = get_object_or_404(Link,id=id)
    instance.delete()
    return redirect("bookmarks:data")