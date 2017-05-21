from django import forms
from addurl.models import Link

class URLform(forms.ModelForm):
    class Meta:
        model = Link
        fields = [
            "url"
        ]