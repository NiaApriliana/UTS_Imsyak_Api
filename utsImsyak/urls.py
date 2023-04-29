from django.contrib import admin
from django.urls import path, include
from utsImsyakApp.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jadwalLombokTimur', jadwalViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
