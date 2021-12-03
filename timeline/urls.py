from .views import WishViewSet, GiftViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"", WishViewSet, basename='wish')
router.register(r"", GiftViewSet, basename='gift')
urlpatterns = router.urls
