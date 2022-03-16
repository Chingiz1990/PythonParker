from django.contrib import admin

# Register your models here.
# zdes' registriruyutsya modeli dlya ih otobrajeniya v admin-paneli
from posts.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)