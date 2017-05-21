from django.conf.urls import url
from addurl.views import (link_list,link_data,link_delete)

urlpatterns = [
    url(r'^$',link_data,name="data"),
    url(r'^add/$',link_list,name="add_url"),
    url(r'^(?P<id>\d+)/delete/$',link_delete,name="delete_url")
]