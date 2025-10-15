from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "email", "created_at", "approved")
    list_filter  = ("approved", "created_at", "post")
    search_fields = ("name", "email", "comment", "post__title")
    list_editable = ("approved",)