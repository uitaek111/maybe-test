from django.contrib import admin
from posts.models import Post, PostImage, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
        "created",
    ]

    inlines = [
        CommentInline,
        PostImageInline,
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
        "created",
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]
