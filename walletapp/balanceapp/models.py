from django.db import models
from userapp.models import User

from walletapp.models import BaseModel

# Create your models here.
class Balance(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_user')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return f"[{self.id}] {self.user.first_name} - {self.amount}"
