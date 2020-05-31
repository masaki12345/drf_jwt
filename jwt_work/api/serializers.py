from rest_framework import serializers
#モデルインポート
from .models import MainContent
from .models import Tag

#メインリストシリアライザ
class MainContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainContent
        #取得フィールド設定
        fields ="__all__"

#サブリストシリアライザ
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        #取得フィールド設定
        fields ="__all__"