from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # this determines what fields are displayed in the post list on admin site
    list_display = ["__str__", "message", "timestamp"]
    list_filter = ["user", "timestamp"]

    class Meta:
        model = Post


# adds Post to admin site
admin.site.register(Post, PostAdmin)
