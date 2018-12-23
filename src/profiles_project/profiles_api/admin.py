from django.contrib import admin

from . import models  #lecture 23

# Register your models here.
admin.site.register(models.UserProfile)     # lecture 23. pass in our model that
# we created to register with the django admin
admin.site.register(models.ProfileFeedItem) # 56
