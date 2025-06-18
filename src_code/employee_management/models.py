from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class Employee(models.Model):
    name = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

    def clean(self):
        # Ensure date_of_joining is less than or equal to the current date
        if self.date_of_joining and self.date_of_joining > now().date():
            raise ValidationError("Date of joining must be less than or equal to the current date.")

    class Meta:
        # Remove the CheckConstraint since it can't evaluate `now().date()` at the database level
        ordering = ['name']
