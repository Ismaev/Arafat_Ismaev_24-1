from django import forms

class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=5)
    description = forms.CharField(weight=forms.Textarea())
    rate = forms.FloatField(required=False)

class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=3)