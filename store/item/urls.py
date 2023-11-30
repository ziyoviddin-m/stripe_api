from django.urls import path, include
from item.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls))
]