from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()

# register the ViewSet
router.register(r'books', BookViewSet, basename='book')

urlpatterns = router.urls