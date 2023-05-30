from rest_framework.routers import DefaultRouter
from .api.user import UserInfoAPIView
from .api.main import (
    ClientViewSet, SiteViewSet, ManufacturerViewSet,
    PartViewSet, LineItemViewSet, WorkOrderViewSet
)

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'sites', SiteViewSet, basename='sites')
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturers')
router.register(r'parts', PartViewSet, basename='parts')
router.register(r'lineitems', LineItemViewSet, basename='lineitems')
router.register(r'workorders', WorkOrderViewSet, basename='workorders')
urlpatterns = router.urls
