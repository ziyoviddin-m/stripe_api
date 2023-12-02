from django.urls import include, path
from rest_framework import routers

from item import views
from item.views import *

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet)

app_name = 'item'

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('success/', SuccessTemplateView.as_view(), name='success'),

    path('buy/<int:item_id>', BuyApi.as_view(), name='buy'),
    path('item/<int:item_id>', ItemApi.as_view()),
]