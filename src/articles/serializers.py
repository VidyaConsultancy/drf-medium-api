from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    is_active = serializers.BooleanField(default=False)
    description = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.description = validated_data.get('description', instance.description)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        
        instance.save()
        return instance
