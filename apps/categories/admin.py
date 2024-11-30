from apps.categories.models import Category, Subcategory as SubCategory
from django.contrib import admin

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)