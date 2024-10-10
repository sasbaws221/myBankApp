from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet,SubscriptionViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Subscription', SubscriptionViewSet)

urlpatterns = [
    path('/', include(router.urls))
]