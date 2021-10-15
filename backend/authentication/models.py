from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import datetime, date

class User(AbstractBaseUser):

    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, blank=True)
    dob = models.DateField(default=date(2000,1,1), blank=True)
    # profile_photo_url = models.URLField(max_length = 200, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=datetime.now)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class FreemiumUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=255, unique = True)
    quota_done = models.BooleanField(default = False)


"""
class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    website = models.URLField(max_length = 255, blank=True)

class FoodType(models.Model):
    food_type_id = models.AutoField(primary_key=True)
    food_type = models.CharField(max_length=255)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_name = models.CharField(max_length = 255)
    food_type_id = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    food_image_url = models.URLField(max_length = 255, blank=True)
    approve_status = models.BooleanField(default=False)
    post_time = models.TimeField(auto_now_add = True)
 

class UserPostLike(models.Model):
    like_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_like = models.BooleanField(default= True)







class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    website = models.URLField(max_length = 255, blank=True)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=255)
    food_type_id = models.CharField(max_length=255)
    food_image_url = models.URLField(max_length = 255, blank=True)
    approve_status = models.BooleanField(default=False)
    

class UserPostLikes(models.Model):
    like_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_like = models.BooleanField(default= True)

class FriendRequest(models.Model):
    request_id = models.AutoField(primary_key = True)
    requester_id = models.ForeignKey(User, on_delete=models.CASCADE)
    requestee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    request_status = models.CharField(default = 'accepted')

class SessionParticipation:
    participation_id = models.AutoField(primary_key = True)
    session_id = models.ForeignKey(GroupFoodieSessions, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

class GroupFoodieSession:
    session_id = models.AutoField(primary_key = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    matched_post_id = models.ForeignKey(Post, on_delete = models.CASCADE)

class PostsTaggingRelationship:
    tagged_id = models.AutoField(primary_key = True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class UserFriendship:
    friendship_id = models.AutoField(primary_key = True)
    user1_id = models.ForeignKey(User, on_delete = models.CASCADE)
    user2_id = models.ForeignKey(User, on_delete = models.CASCADE)
    is_friend = models.BooleanField(default = True)

"""









"""
class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    website = models.URLField(max_length = 255, blank=True)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=255)
    food_type_id = models.CharField(max_length=255)
    food_image_url = models.URLField(max_length = 255, blank=True)
    approve_status = models.BooleanField(default=False)
    

class UserPostLikes(models.Model):
    like_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_like = models.BooleanField(default= True)

class FriendRequest(models.Model):
    request_id = models.AutoField(primary_key = True)
    requester_id = models.ForeignKey(User, on_delete=models.CASCADE)
    requestee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    request_status = models.CharField(default = 'accepted')

class SessionParticipation:
    participation_id = models.AutoField(primary_key = True)
    session_id = models.ForeignKey(GroupFoodieSessions, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

class GroupFoodieSession:
    session_id = models.AutoField(primary_key = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    matched_post_id = models.ForeignKey(Post, on_delete = models.CASCADE)

class PostsTaggingRelationship:
    tagged_id = models.AutoField(primary_key = True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class UserFriendship:
    friendship_id = models.AutoField(primary_key = True)
    user1_id = models.ForeignKey(User, on_delete = models.CASCADE)
    user2_id = models.ForeignKey(User, on_delete = models.CASCADE)
    is_friend = models.BooleanField(default = True)

"""








