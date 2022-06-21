from django.contrib import admin

from .models import Tag, Post,CommentModel

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(CommentModel)