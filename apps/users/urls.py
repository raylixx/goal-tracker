from django.urls import path, include
from rest_framework import routers

from apps.users.views import hello_world, GoalListApiView, StepDetailApiView, GoalDetailApiView, \
    GoalListApiView, GoalViewSet
from goal_tracker.urls import urlpatterns

router = routers.DefaultRouter()
router.register('goals-viewset', GoalViewSet)


urlpatterns = [
    path('/hello', hello_world),
    path('goal', GoalListApiView.as_view(), name = 'goal-list'),
]