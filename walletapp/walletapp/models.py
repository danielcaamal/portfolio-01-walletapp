from django.db import models
from userapp.models import User

class BaseModel(models.Model):
    """Base model for all models in the project."""
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    
    class Meta:
        abstract = True