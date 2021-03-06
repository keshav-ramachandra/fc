from rest_framework import serializers

from .models import User
# from .models import Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  User
        fields = ('user_name', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'dob', )




# class SwipeDataSerializer(serializers.HyperlinkedModelSerializer):
#     restaurant_name = serializers.CharField(source='restaurant_id.name')
#     user_name = serializers.CharField(source='restaurant_id.name')
#     food_type = serializers.CharField(source='food_type_id.food_type')
#     class Meta:
#         model =  Post
#         fields = ['user_name','restaurant_name', 'food_type', 'food_name']

