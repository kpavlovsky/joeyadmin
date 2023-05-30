"""API Viewsets for the main app."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from main import models
from main.serializers.main import (
    ClientSerializer,
    SiteSerializer,
    ManufacturerSerializer,
    PartSerializer,
    LineItemSerializer,
    WorkOrderSerializer,
)


class ClientViewSet(viewsets.ModelViewSet):
    """API endpoint that allows clients to be viewed or edited."""

    queryset = models.Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


class SiteViewSet(viewsets.ModelViewSet):
    """API endpoint that allows sites to be viewed or edited."""

    queryset = models.Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]


class ManufacturerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows manufacturers to be viewed or edited."""

    queryset = models.Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated]


class PartViewSet(viewsets.ModelViewSet):
    """API endpoint that allows parts to be viewed or edited."""

    queryset = models.Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [IsAuthenticated]


class LineItemViewSet(viewsets.ModelViewSet):
    """API endpoint that allows line items to be viewed or edited."""

    queryset = models.LineItem.objects.all()
    serializer_class = LineItemSerializer
    permission_classes = [IsAuthenticated]


class WorkOrderViewSet(viewsets.ModelViewSet):
    """API endpoint that allows work orders to be viewed or edited."""

    queryset = models.WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
    permission_classes = [IsAuthenticated]
