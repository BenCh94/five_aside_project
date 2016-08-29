from django import forms


class PaymentMethodForm(forms.Form):
    MONTH_CHOICES = [(i, i,) for i in xrange(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in xrange(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code(cvv)')
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
