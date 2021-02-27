from django.urls import path, include
from django.contrib import admin
from god.urls import router
from rest_framework.authtoken import views
from .yasg import urlpatterns as docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', views.obtain_auth_token, name='api-token-auth')
]

urlpatterns += docs
