from django.contrib import admin
from .models import User,UserProfile, Business, Investment, Conversation, Sector

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Investment)
admin.site.register(Conversation)
admin.site.register(Sector)