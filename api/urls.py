from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from request_handler.urls import urlpatterns as api_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
