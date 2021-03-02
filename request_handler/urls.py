from django.urls import path
from rest_framework.authtoken import views
from api.yasg import urlpatterns as docs
from request_handler.views import ServiceView, ServiceStatusView, LogView, ServiceInterfaceView, ServiceInterfacesView

s = 'service'
l = 'logs'

urlpatterns = [
    path('auth/', views.obtain_auth_token, name='api-token-auth'),
    path(f'{s}/', ServiceView.as_view({'get': 'list'})),
    path(f'{s}/<int:pk>/', ServiceView.as_view({'get': 'retrieve'})),
    path(f'{s}/create/', ServiceView.as_view({'post': 'create'})),
    path(f'{s}/update/status/<int:pk>/', ServiceStatusView.as_view({'post': 'partial_update'})),
    path(f'{s}/update/interface/<int:pk>/', ServiceInterfaceView.as_view({'post': 'partial_update'})),
    path(f'{s}/update/interfaces/<int:pk>/', ServiceInterfacesView.as_view({'post': 'partial_update'})),
    path(f'{s}/delete/<int:pk>/', ServiceView.as_view({'delete': 'destroy'})),

    path(f'{l}/', LogView.as_view({'get': 'list'})),
    path(f'{l}/<int:pk>/', LogView.as_view({'get': 'retrieve'})),
    path(f'{l}/create/', LogView.as_view({'post': 'create'}))
]

urlpatterns += docs
