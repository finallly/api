from django.urls import path
from rest_framework.authtoken import views
from api.yasg import urlpatterns as docs
from god.views import ServiceView


urlpatterns = [
    path('auth/', views.obtain_auth_token, name='api-token-auth'),
    path('services/', ServiceView.as_view({'get': 'list'})),
    path('services/<int:pk>/', ServiceView.as_view({'get': 'retrieve'}))
]

urlpatterns += docs
