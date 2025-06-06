from django import forms
from datetime import date
from .models import Employee  # Assuming you have an Employee model.

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'department', 'date_of_joining']
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'date_of_joining': 'Date of Joining',
        }

    def clean_date_of_joining(self):
        date_of_joining = self.cleaned_data.get('date_of_joining')
        if date_of_joining and date_of_joining > date.today():
            raise forms.ValidationError("Date of Joining cannot be in the future.")
        return date_of_joining
