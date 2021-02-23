from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]