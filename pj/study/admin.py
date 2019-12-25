from django.contrib import admin
from .models import *

# Register your models here.

class createContent(admin.TabularInline):
    model = BlogContent

class createBlog(admin.ModelAdmin):
    inlines = [createContent]
    fieldsets = (
        (None, {
            "fields": (
                'title',
                'slug',
                'discription',
                'kind',
            ),
        }),
    )
    

admin.site.register(Blog, createBlog)


