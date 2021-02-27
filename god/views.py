import json

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.http import JsonResponse

from .models import ServiceModel
from .serializers import ServiceSerializer
from .models import ServiceModel as model


class ServiceView(viewsets.GenericViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk):
        queryset = self.get_queryset()
        try:
            service = queryset.get(pk=pk)
            serializer = ServiceSerializer(service)
            return Response(serializer.data, status=200)
        except model.DoesNotExist:
            return JsonResponse(data={'error': 'such service does not exist'}, status=404)

    def create(self, request):
        pass
