from django.urls import path
from rest_framework.authtoken import views
from api.yasg import urlpatterns as docs
from god.views import ServiceView, LogView

urlpatterns = [
    path('auth/', views.obtain_auth_token, name='api-token-auth'),
    path('services/', ServiceView.as_view({'get': 'list'})),
    path('services/<int:pk>/', ServiceView.as_view({'get': 'retrieve'})),
    path('services/create/', ServiceView.as_view({'post': 'create'})),
    path('services/update/<int:pk>/', ServiceView.as_view({'post': 'partial_update'})),
    path('services/delete/<int:pk>/', ServiceView.as_view({'delete': 'destroy'})),
    path('logs/', LogView.as_view({'get': 'list'})),
    path('logs/<int:pk>/', LogView.as_view({'get': 'retrieve'})),
    path('logs/create/', LogView.as_view({'post': 'create'}))
]

urlpatterns += docs
