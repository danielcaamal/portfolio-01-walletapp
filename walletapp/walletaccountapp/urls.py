from rest_framework.routers import DefaultRouter
from . import views

app_name = 'wallet_account'

router = DefaultRouter()
router.register(r'', views.WalletAccountViewSet, basename='wallet_account')
router.register(r'user/(?P<user_id>[0-9]+)', views.WalletAccountByUserViewSet, basename='wallet_account_by_user')
router.register(r'balance/(?P<balance_id>[0-9]+)', views.WalletAccountByBalanceViewSet, basename='wallet_account_by_balance')

urlpatterns = router.urls
