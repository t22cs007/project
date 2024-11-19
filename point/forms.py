# forms.py (contributionApp)
from django import forms
from .models import Point

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['activity_name', 'description', 'points_requested', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'activity_name': '活動名',
            'description': '活動内容',
            'points_requested': '申請ポイント数',
            'date': '活動日',
        }
