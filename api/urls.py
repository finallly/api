from django.urls import path, include
from django.contrib import admin
from .yasg import urlpatterns as docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('god.urls'))
]

urlpatterns += docs
