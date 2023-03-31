from rest_framework import viewsets
from .models import Balance
from .serializers import BalanceSerializer

# Create your views here.
class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class BalanceByUserViewSet(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Balance.objects.filter(user=user_id)