from rest_framework import serializers
from mysite.models import Categorys, Titles, Thinkings, Feelings, Emotions, Behaviors

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        # fields = ('id', 'category')
        fields = '__all__'
    

class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = ('id', 'title', )


class ThinkingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thinkings
        fields = ('id', 'thinking', 'title')


class FeelingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feelings
        fields = ('id', 'feeling', 'title')


class EmothionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotions
        fields = ('id', 'emothin', 'title')


class BehaviorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behaviors
        fields = ('id', 'behavior', 'title')