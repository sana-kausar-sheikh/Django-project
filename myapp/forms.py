from django import forms 
from .models import Membernew

class MemberForm(forms.Form):
    class Meta:
        model=Membernew
        fields=['firstname','lastname','image','rollno','phoneno']