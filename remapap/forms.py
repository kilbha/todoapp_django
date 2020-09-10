from django import forms
from remapap.models import todo
class todoform(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(
        attrs={'style': 'resize:none;', 'rows': 2, 'cols':50, 'class': 'border-1 rounded mt-2 w-50',
               'placeholder': "  Enter Your task"}), label='')
    class Meta:
        model = todo
        fields = "__all__"