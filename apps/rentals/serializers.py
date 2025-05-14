from django.db.migrations import AlterModelOptions
from rest_framework import serializers
from .models import *

class GoalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            'id',
            'name',
            'surname',
        ]


class StepSerializer(serializers.ModelSerializer):
    Goal = GoalSerializer()
    class Meta:
        model = Step
        fields = "__all__"


