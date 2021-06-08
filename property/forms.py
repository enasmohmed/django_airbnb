from django import forms
from django.forms import inlineformset_factory

from property.models import PropertyBook, PropertyReview, Property, PropertyImages


class PropertyBookForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'id': 'date-start'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'id': 'date-end'}))

    class Meta:
        model = PropertyBook
        fields = ['date_from', 'date_to', 'guest', 'children']


class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = PropertyReview
        fields = ['rate','feedback']


class PropertyImageFormset(forms.ModelForm):
    class Meta:
        model = PropertyImages
        fields = ['property', 'image']


PropertyImageFormset = inlineformset_factory(
    Property,
    PropertyImages,
    form=PropertyImageFormset,
    fields=['image'],
    extra=2,
    can_delete=True
)


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ('slug', 'owner')