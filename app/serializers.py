from rest_framework_mongoengine import serializers
from app.models import Movie

class MovieGetSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Movie
        exclude = ['id']

class MovieSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
