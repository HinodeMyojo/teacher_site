from django import forms


class SignForm(forms.Form):
    first_name = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'take_a_class_inside_block_input_box',
                'placeholder': 'Например: Иван'
                }
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'take_a_class_inside_block_input_box',
                'placeholder': 'Например: Иванов'
                }
        )
    )
    date = forms.DateTimeField(
        label='Дата',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'take_a_class_inside_block_input_box'
                }
            )
    )
