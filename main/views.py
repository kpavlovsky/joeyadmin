from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from . import models
from .forms import WorkOrderForm, ClientForm, ManufacturerForm, PartForm, LineItemForm


# Create your views here.

class WorkOrderList(LoginRequiredMixin, ListView):
    template_name = 'main/workorder_list.html'
    context_object_name = 'workorders'

    def get_queryset(self):
        return self.request.user.workorder_set.all()


class WorkOrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/form.html'
    model = models.WorkOrder
    form_class = WorkOrderForm
    success_url = '/workorders/'


class WorkOrderUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'main/workorder_edit.html'
    model = models.WorkOrder
    form_class = WorkOrderForm
    success_url = '/workorders/'


class ClientList(LoginRequiredMixin, ListView):
    template_name = 'main/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return models.Client.objects.all()


class ClientCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/form.html'
    model = models.Client
    form_class = ClientForm
    success_url = '/clients/'


class SiteList(LoginRequiredMixin, ListView):
    template_name = 'main/site_list.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return models.Site.objects.all()


class SiteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/form.html'
    model = models.Site
    fields = ['client', 'site_name', 'slug', 'address', 'note']
    success_url = '/sites/'


class ManufacturerListView(LoginRequiredMixin, ListView):
    template_name = 'main/manufacturer_list.html'
    context_object_name = 'manufacturers'

    def get_queryset(self):
        return models.Manufacturer.objects.all()


class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/form.html'
    model = models.Manufacturer
    form_class = ManufacturerForm
    success_url = '/manufacturers/'


class PartListView(LoginRequiredMixin, ListView):
    template_name = 'main/part_list.html'
    context_object_name = 'parts'

    def get_queryset(self):
        return models.Part.objects.all()


class PartCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/form.html'
    model = models.Part
    form_class = PartForm
    success_url = '/parts/'


class LineItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/form.html'
    model = models.LineItem
    form_class = LineItemForm
    object: models.LineItem

    def success_url(self):
        return f'/workorders/{self.object.work_order.pk}'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.work_order = models.WorkOrder.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return super().form_valid(form)
