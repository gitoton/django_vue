from rest_framework import viewsets

from mysite.models import Categorys, Titles, Thinkings, Feelings, Emotions, Behaviors
from mysite.serializers import CategorySerializer, TitlesSerializer, ThinkingsSerializer, FeelingsSerializer, EmothionsSerializer, BehaviorsSerializer

class CategorysViewSet(viewsets.ModelViewSet):
    """API endpoint for Categorys"""
    queryset = Categorys.objects.all()
    serializer_class = CategorySerializer


class TitlesViewSet(viewsets.ModelViewSet):
    """API endpoint for Titles"""
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer


class ThinkingsViewSet(viewsets.ModelViewSet):
    """API endpoint for Thinkings"""
    queryset = Thinkings.objects.all()
    serializer_class = ThinkingsSerializer


class FeelingsViewSet(viewsets.ModelViewSet):
    """API endpoint for Feelings"""
    queryset = Feelings.objects.all()
    serializer_class = FeelingsSerializer


class EmotionsViewSet(viewsets.ModelViewSet):
    """API endpoint for Emotions"""
    queryset = Emotions.objects.all()
    serializer_class = EmothionsSerializer


class BehaviorsViewSet(viewsets.ModelViewSet):
    """API endpoint for Behaviors"""
    queryset = Behaviors.objects.all()
    serializer_class = BehaviorsSerializer