from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import VoucherViewSet, ProductViewSet, OrderViewSet, HistoryViewSet

router = routers.DefaultRouter()

router.register('voucher', VoucherViewSet)
router.register('product', ProductViewSet)
router.register('order', OrderViewSet)
router.register('history', HistoryViewSet)

urlpatterns = [
    path('',include(router.urls))
]