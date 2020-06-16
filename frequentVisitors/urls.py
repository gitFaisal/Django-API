from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.VisitView)

urlpatterns = [
    # path('', views.Index, name= 'home'),
    path('', include(router.urls)),
]
