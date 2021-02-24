from django.urls import path
from god.views import TestView

urlpatterns = [
    path('test/', TestView.as_view()),
]
