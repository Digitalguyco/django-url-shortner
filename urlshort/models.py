from django.db import models

# Importing The Follow Come User Model to Use as a ForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Url(models.Model):
    user = models.ForeignKey(User, related_name='links', blank=True, null=True, on_delete=models.CASCADE) # User
    link = models.CharField(max_length=10000) # Link to be Shortend 
    uuid = models.CharField(max_length=10) # uuid as a charfield 
    created_at = models.DateTimeField(auto_now_add=True) # For ordering purpose
    
    # Meta of Url Model
    class Meta:
        ordering = ('-created_at',) # Order by created_at descending

    # String  Representation of Url Model
    def __str__(self) -> str:
        return self.uuid 

    