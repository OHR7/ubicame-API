from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from profiles.api.views import ProfileViewSet, ProfileAPIView


app_name = 'profiles'
router = routers.SimpleRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'profile/$', ProfileAPIView.as_view(), name='profile-api-view')
]