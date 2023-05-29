from django.contrib.auth import get_user_model
from django.db import models
import requests
import logging

from smart_selects.db_fields import GroupedForeignKey, ChainedForeignKey

from main.tuples import WEBHOOK_TYPE_CHOICES, WEBHOOK_TYPES

User = get_user_model()
logger = logging.getLogger(__name__)


class Client(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ('name', '-pk',)


class Site(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField()
    address = models.CharField(max_length=255, blank=True, null=False)
    note = models.TextField(blank=True, default='')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'


def next_id():
    try:
        obj = WorkOrder.objects.latest('id')
        return obj.id + 1
    except WorkOrder.DoesNotExist:
        return 1


class WorkOrder(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled'),
        ('in_progress', 'In Progress'),
    )
    id = models.IntegerField(primary_key=True, default=next_id)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=False)
    site = ChainedForeignKey(
        Site,
        chained_field='client',
        chained_model_field='client',
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE)
    slug = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    scope = models.TextField(blank=True, null=False)
    status = models.CharField(max_length=255, default='open', choices=STATUS_CHOICES, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_webhook_sent = models.BooleanField(default=False)
    webhook_type = models.IntegerField(choices=WEBHOOK_TYPE_CHOICES, default=WEBHOOK_TYPES.project, verbose_name='Type')

    def __str__(self):
        return self.title

    def generate_slug(self):
        title_slug = self.title.replace(" ", "_")
        self.slug = f"{self.id}-{self.site.client.slug}-{self.site.slug}-{title_slug}"

    def send_webhooks(self):
        data = {
            "work_order_title": self.title,
            "work_order_order_id": self.order_id,
            "work_order_slug": self.slug,
            "work_order_scope": self.scope,
            "work_order_status": self.get_status_display(),
            "work_order_created_at": str(self.created_at),
            "work_order_created_by": self.created_by and self.created_by.email,
            "site_name": self.site.site_name,
            "site_slug": self.site.slug,
            "site_address": self.site.address,
            "client_name": self.site.client.name,
            "client_slug": self.site.client.slug,
        }
        qs = WebHook.objects.filter(webhook_type=self.webhook_type)
        for webhook in qs:
            logger.debug(f"probably need to send {data} something to {webhook.url}")
            try:
                logger.debug(requests.post(url=webhook.url, data=data))
            except Exception as e:
                logger.error(f"While sending webhook for {self.pk} {webhook.url} {str(e)}")

    @property
    def order_id(self):
        if not self.pk:
            return "----"
        return f"{self.pk:04d}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.is_webhook_sent:
            self.generate_slug()
            super().save()
            self.send_webhooks()
            self.is_webhook_sent = True
            super().save(update_fields=['is_webhook_sent', ])

    class Meta:
        verbose_name = 'Work Order'
        verbose_name_plural = 'Work Orders'


class WebHook(models.Model):
    title = models.CharField(default='', max_length=255)
    webhook_type = models.IntegerField(choices=WEBHOOK_TYPE_CHOICES, default=WEBHOOK_TYPES.project, verbose_name='Type')
    url = models.CharField(max_length=255, blank=False, null=False)
    note = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title or self.url

    class Meta:
        verbose_name = 'Webhook'
        verbose_name_plural = 'Webhooks'


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField()
    note = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'
        ordering = ('name', '-pk',)


class Part(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, default='')
    part_number = models.CharField(max_length=255, blank=True, default='')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    note = models.TextField(blank=True, default='')
    link = models.URLField(blank=True, default='')

    def __str__(self):
        return self.manufacturer.name + " " + self.name

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'
        ordering = ('name', '-pk',)


class LineItem(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    description = models.TextField(blank=True, default='')
    location = models.CharField(max_length=255, blank=True, default='')
    quantity = models.IntegerField(default=1)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    extended_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    source = models.TextField(max_length=255, blank=True, default='')
    note = models.TextField(blank=True, default='')
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.part} x {self.quantity}"

    class Meta:
        verbose_name = 'Line Item'
        verbose_name_plural = 'Line Items'
        ordering = ('part', '-pk',)
