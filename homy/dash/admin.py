from django.contrib import admin # type: ignore
from .models import ChefOffering , Dish, User

# from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'latitude', 'longitude', 'additional_details']  # Add fields to display in the list
    search_fields = ['name', 'phone_number']  # Allow searching by phone number
    list_filter = ['latitude', 'longitude']  # Add filters if necessary

admin.site.register(ChefOffering)
admin.site.register(Dish)
admin.site.register(User, UserAdmin)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'latitude', 'longitude') 