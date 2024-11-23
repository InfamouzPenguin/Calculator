from django import forms

class CalculatorForm(forms.Form):
    OPERATIONS = [
        ('add', 'Add'),
        ('subtract', 'Subtract'),
        ('multiply', 'Multiply'),
        ('divide', 'Divide'),
        ('exponent', 'Exponent'),
        ('modulus', 'Modulus'),
    ]

    number1 = forms.FloatField(
        label='Number 1',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter first number',
            'required': True,
        })
    )
    number2 = forms.FloatField(
        label='Number 2',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter second number',
            'required': True,
        })
    )
    operation = forms.ChoiceField(
        choices=OPERATIONS,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_operation',
        })
    )
