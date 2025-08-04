# djangoapp/admin.py
from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 3  # Number of extra forms to display

# CarModelAdmin class
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']
    list_filter = ['car_make', 'type', 'year', 'dealer_id']
    search_fields = ['name', 'car_make__name']
    ordering = ['car_make__name', 'name']
    
    # Grouping fields in the admin form
    fieldsets = [
        ('Basic Information', {
            'fields': ['car_make', 'name', 'type', 'year']
        }),
        ('Details', {
            'fields': ['dealer_id'],
            'classes': ['collapse']
        })
    ]

# CarMakeAdmin class with CarModelInline
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['name']
    
    # Include CarModel inline forms
    inlines = [CarModelInline]
    
    # Grouping fields in the admin form
    fieldsets = [
        ('Company Information', {
            'fields': ['name', 'description']
        })
    ]