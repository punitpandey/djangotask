from django import forms
class teacherForm(forms.Form):
    name=forms.CharField(max_length="50")
    notify_id=forms.CharField(max_length="50",required=False)
