from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

# Create your models here.
class cust_login(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)

    def save(self, *args, **kwargs):
        if not self.pk:  # If it's a new object
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}"