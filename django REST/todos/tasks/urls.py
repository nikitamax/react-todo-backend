from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from tasks import views

urlpatterns = [
    url(r'^api/tasks/$', views.tasks_list),
    url(r'^api/tasks/(?P<pk>[0-9]+)/$', views.task_detail),
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)