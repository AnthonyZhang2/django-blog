from django.contrib import admin
from blogging.models import Post, Category

"""
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post)
admin.site.register(Category)

"""


class InlineModelAdmin(admin.TabularInline):
    model = Category.posts.through


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    inlines = [
        InlineModelAdmin,
    ]
    exclude = ("posts",)


class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author", "published_date")
    inlines = [
        InlineModelAdmin,
    ]


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Post, PostModelAdmin)
