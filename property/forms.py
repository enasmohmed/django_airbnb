from django import forms

from property.models import PropertyBook, PropertyReview


class PropertyBookForm(forms.ModelForm):
    class Meta:
        model = PropertyBook
        fields = ['date_from', 'date_to', 'guest', 'children']


class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = PropertyReview
        fields = ['rate','feedback']