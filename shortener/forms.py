from django import forms
from .models import URL

class URLForm(forms.ModelForm):
    custom_alias = forms.CharField(required=False, max_length=6, label='Custom Alias (Optional)')

    class Meta:
        model = URL
        fields = ['original_url', 'custom_alias']
