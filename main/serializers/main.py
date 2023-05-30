# serializers for the main app

from rest_framework import serializers
from main import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'name', 'slug']


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Site
        fields = ['id', 'client', 'site_name', 'slug', 'address', 'note']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ['id', 'name', 'slug', 'note']


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Part
        fields = ['id', 'manufacturer', 'name', 'description', 'cost', 'part_number', 'note', 'link', ]


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LineItem
        fields = [
            'id',
            'part',
            'description',
            'location',
            'quantity',
            'cost',
            'extended_cost',
            'source',
            'note',
            'work_order',
            'item_price',
        ]


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkOrder
        fields = [
            'id',
            'site',
            'client',
            'slug',
            'title',
            'scope',
            'status',
            'created_at',
            'created_by',
        ]
