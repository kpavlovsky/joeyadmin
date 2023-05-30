from django.urls import path
from django.views.generic import RedirectView

from .api.user import UserInfoAPIView
from .views import WorkOrderList, WorkOrderCreateView, ClientList, ClientCreateView, SiteList, SiteCreateView, \
    ManufacturerListView, ManufacturerCreateView, PartListView, PartCreateView, WorkOrderUpdateView, LineItemCreateView

urlpatterns = [
    path('', RedirectView.as_view(url='/workorders/', permanent=True)),
    path('parts/', PartListView.as_view(), name='parts'),
    path('parts/create', PartCreateView.as_view(), name='parts_create'),
    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturers'),
    path('manufacturers/create', ManufacturerCreateView.as_view(), name='manufacturers_create'),
    path('sites/', SiteList.as_view(), name='sites'),
    path('sites/create', SiteCreateView.as_view(), name='sites_create'),
    path('clients/', ClientList.as_view(), name='clients'),
    path('clients/create', ClientCreateView.as_view(), name='clients_create'),
    path('workorders/create', WorkOrderCreateView.as_view(), name='workorders_create'),
    path('workorders/<pk>', WorkOrderUpdateView.as_view(), name='workorders_edit'),
    path('workorders/<pk>/add_line_item', LineItemCreateView.as_view(), name='workorders_add_line_item'),
    path('workorders/', WorkOrderList.as_view(), name='workorders'),
    path('user/info', UserInfoAPIView.as_view(), name='user_info'),
]
