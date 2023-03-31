from rest_framework.routers import DefaultRouter
from . import views

app_name = 'balance'

router = DefaultRouter()
router.register(r'', views.BalanceViewSet, basename='balance')
router.register(r'user/(?P<user_id>[0-9]+)', views.BalanceByUserViewSet, basename='balance_by_user')

urlpatterns = router.urls
