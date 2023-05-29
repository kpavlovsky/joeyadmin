from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models


# Create your views here.

class WorkOrderList(LoginRequiredMixin, ListView):
    template_name = 'main/workorder_list.html'
    context_object_name = 'workorders'

    def get_queryset(self):
        return self.request.user.workorder_set.all()


class WorkOrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/workorder_create.html'
    model = models.WorkOrder
    fields = ['title', 'scope', 'client', 'site', 'status']
    success_url = '/workorders/'
