from django.conf.urls import url
from . import views                     # the '.' means the root location


urlpatterns = [
    url(r'^hello-view/',views.HelloApiView.as_view()),
]
