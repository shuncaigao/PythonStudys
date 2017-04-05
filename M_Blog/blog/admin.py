from django.contrib import admin

from blog.models import User, Tag, Article, Links, Comment, Ad, Category


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 默认显示这三个字段
    fields = ('title', 'desc', 'content')


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
