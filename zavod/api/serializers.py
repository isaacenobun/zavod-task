from .models import User, News, Tags
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(queryset=News.objects.all(), many=True)
    class Meta:
        model = User
        fields = '__all__'
        depth = 2
    
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        depth = 1
        
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'