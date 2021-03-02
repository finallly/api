from django.urls import path
from rest_framework.authtoken import views
from api.yasg import urlpatterns as docs
from request_handler.views import ServiceView, ServiceStatusView, LogView, ServiceInterfaceView, ServiceInterfacesView,\
    StatisticsView

se = 'service'
lo = 'log'
st = 'statistics'

urlpatterns = [
    # service urls
    path('auth/', views.obtain_auth_token, name='api-token-auth'),
    path(f'{se}/list/', ServiceView.as_view({'get': 'list'})),
    path(f'{se}/<int:pk>/', ServiceView.as_view({'get': 'retrieve'})),
    path(f'{se}/create/', ServiceView.as_view({'post': 'create'})),
    path(f'{se}/update/status/<int:pk>/', ServiceStatusView.as_view({'post': 'partial_update'})),
    path(f'{se}/update/interface/<int:pk>/', ServiceInterfaceView.as_view({'post': 'partial_update'})),
    path(f'{se}/update/interfaces/<int:pk>/', ServiceInterfacesView.as_view({'post': 'partial_update'})),
    path(f'{se}/delete/<int:pk>/', ServiceView.as_view({'delete': 'destroy'})),

    # log urls
    path(f'{lo}/list/', LogView.as_view({'get': 'list'})),
    path(f'{lo}/<int:pk>/', LogView.as_view({'get': 'retrieve'})),
    path(f'{lo}/create/', LogView.as_view({'post': 'create'})),

    # statistics urls
    path(f'{st}/list/', StatisticsView.as_view({'get': 'list'})),
    path(f'{st}/<int:pk>/', StatisticsView.as_view({'get': 'retrieve'})),
    path(f'{st}/create/', StatisticsView.as_view({'post': 'create'}))
]

urlpatterns += docs
