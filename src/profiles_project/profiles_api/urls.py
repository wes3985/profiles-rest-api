from django.conf.urls import url
from django.conf.urls import include   #36
from rest_framework.routers import DefaultRouter        # 36
from . import views                     # the '.' means the root location


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')  #36
router.register('profile', views.UserProfileViewSet)    #43
router.register('login', views.LoginViewSet, base_name='login') #50
router.register('feed', views.UserProfileFeedViewSet) # 58

urlpatterns = [
    url(r'^hello-view/',views.HelloApiView.as_view()),
    url(r'', include(router.urls))  # 36    # checks what we pass in first, then checks urls in the router.
]
