from django.contrib import admin

# Register your models here.
#メインリストインポート
from .models import MainContent
#サブリストインポート
from .models import Tag

#メイン・サブリストを管理画面上に表示
admin.site.register(MainContent)
admin.site.register(Tag)