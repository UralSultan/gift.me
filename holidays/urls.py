from .views import HolidayViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"", HolidayViewSet, basename='holidays')
urlpatterns = router.urls
