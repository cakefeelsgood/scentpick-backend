from django.contrib import admin
from django.utils.html import format_html
from .models import MainContent, Comment

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date', 'image_preview']
    search_fields = ['title']

    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px;" />', obj.image.url)
        return "(No image)"

    image_preview.short_description = '이미지 미리보기'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author__username']  # author는 ForeignKey니까 필드 지정

admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, CommentAdmin)
