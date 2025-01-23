from django.contrib import admin
from .models import Blogging,Category,Comment

# Register your models here.
admin.site.register(Blogging)
admin.site.register(Category)
admin.site.register(Comment)
