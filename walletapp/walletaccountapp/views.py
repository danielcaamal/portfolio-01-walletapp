from rest_framework import viewsets
from .models import WalletAccount
from .serializers import WalletAccountSerializer

# Create your views here.
class WalletAccountViewSet(viewsets.ModelViewSet):
    queryset = WalletAccount.objects.all()
    serializer_class = WalletAccountSerializer


class WalletAccountByUserViewSet(viewsets.ModelViewSet):
    serializer_class = WalletAccountSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return WalletAccount.objects.filter(balance__user__id=user_id)

class WalletAccountByBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = WalletAccountSerializer

    def get_queryset(self):
        balance_id = self.kwargs['balance_id']
        return WalletAccount.objects.filter(balance__id=balance_id)