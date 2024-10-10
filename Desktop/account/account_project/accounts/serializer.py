from rest_framework import serializers
from accounts.models import User,Subscription


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ('fullName','email','password','company')



class SubscriptionSerializer(serializers.ModelSerializer):
  
    class Meta :
         model = Subscription
         fields =('package','description','monthlyPrice','yearlyPrice')


