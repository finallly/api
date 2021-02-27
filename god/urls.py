from rest_framework import routers
from god.views import CreateServiceView


router = routers.DefaultRouter()
router.register('service/create', CreateServiceView)