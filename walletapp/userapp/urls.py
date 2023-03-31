from rest_framework.routers import DefaultRouter
from . import views

app_name = 'User'

router = DefaultRouter()
# router.register(r'', views.UserViewSet, basename='User')

urlpatterns = router.urls
