from django.urls import path
from .api.user import UserInfoAPIView
from .views import WorkOrderList, WorkOrderCreateView, ClientList, ClientCreateView, SiteList, SiteCreateView

urlpatterns = [

    path('sites/', SiteList.as_view(), name='sites'),
    path('sites/create', SiteCreateView.as_view(), name='sites_create'),
    path('clients/', ClientList.as_view(), name='clients'),
    path('clients/create', ClientCreateView.as_view(), name='clients_create'),
    path('workorders/create', WorkOrderCreateView.as_view(), name='workorders_create'),
    path('workorders/', WorkOrderList.as_view(), name='workorders'),
    path('user/info', UserInfoAPIView.as_view(), name='user_info'),
]
