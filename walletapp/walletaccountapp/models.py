from django.db import models

from walletapp.models import BaseModel

WALLET_CATEGORIES = (
    ("0", "Income"), 
    ("1", "Expense"),
)

# Create your models here.
class WalletAccount(BaseModel):
    description = models.CharField(max_length=100, default="Balance")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_hidden = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default="#000000")
    icon = models.CharField(max_length=50, default="fa fa-money")
    wallet_category = models.CharField(choices=WALLET_CATEGORIES, default="0", max_length=1)
    balance = models.ForeignKey("balanceapp.Balance", on_delete=models.CASCADE, related_name='%(class)s_balance')
    
    def __str__(self):
        return f"[{self.id}] {self.description} - {self.amount}"
