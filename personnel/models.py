from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=32)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Personnel(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    GENDER = (
        ("M","Male"),
        ("F", "Female"),
        ("N","Prefer Not To Say"),
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    title
    salary
    started
    department_id
    user_id
    created
    updated
                            
