from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from main.models import WorkOrder, Client, Site, Manufacturer, Part, LineItem


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


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['client', 'site_name', 'slug', 'address', 'note']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'slug', 'note']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['manufacturer', 'name', 'description', 'cost', 'note', 'link', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


class LineItemForm(forms.ModelForm):
    class Meta:
        model = LineItem
        fields = [
            'part',
            'description',
            'location',
            'quantity',
            'cost',
            'extended_cost',
            'source',
            'note',
            'item_price',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
