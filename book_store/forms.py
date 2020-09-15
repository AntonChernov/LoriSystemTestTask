from django import forms
from book_store.models import Book


class AddToCartForm(forms.Form):
    item_slug = forms.CharField(widget=forms.HiddenInput)
    rent_days = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        super(AddToCartForm, self).__init__(*args, **kwargs)

    def clean(self):
        item_slug = self.cleaned_data['item_slug']
        rent_days = self.cleaned_data['rent_days']

        if not Book.objects.filter(slug=item_slug).exists():
            raise forms.ValidationError("Book not found!")
        if rent_days < 0:
            raise forms.ValidationError("Rent days < 0")
