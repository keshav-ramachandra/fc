from django.contrib import admin
from .models import User
# from .models import Restaurant
# from .models import UserPostLike
# from .models import Post
# from .models import FoodType
from .models import FreemiumUser
# Register your models here.

admin.site.register(User)
# admin.site.register(Restaurant)
# admin.site.register(UserPostLike)
# admin.site.register(Post)
# admin.site.register(FoodType)
admin.site.register(FreemiumUser)