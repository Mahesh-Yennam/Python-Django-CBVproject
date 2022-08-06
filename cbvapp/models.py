from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    contact=models.CharField(max_length=20)
    address=models.TextField(max_length=200)

    def __str__(self):
        return self.name
    

from django import forms

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__"

