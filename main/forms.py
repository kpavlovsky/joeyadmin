from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from main.models import WorkOrder, Client


class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['title', 'scope', 'client', 'site', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
