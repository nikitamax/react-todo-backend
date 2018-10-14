from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^api/tasks/$', views.snippet_list),
    url(r'^api/tasks/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)