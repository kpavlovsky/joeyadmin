from django.urls import path
from .api.user import UserInfoAPIView
from .views import WorkOrderList
urlpatterns = [
    path('workorders/', WorkOrderList.as_view(), name='workorders'),
    path('user/info', UserInfoAPIView.as_view(), name='user_info'),
]
