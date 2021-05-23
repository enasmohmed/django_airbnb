from django import forms

from property.models import PropertyBook


class PropertyBookForm(forms.ModelForm):
    class Meta:
        model = PropertyBook
        fields = ['date_from', 'date_to', 'guest', 'children']