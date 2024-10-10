from rest_framework import viewsets
from accounts.models import User,Subscription
from accounts.serializer import UserSerializer,SubscriptionSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    


