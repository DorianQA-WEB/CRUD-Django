from django import forms


class UserForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        max_length=20,
        label="Имя пользователя",
        initial='undefined',
        help_text='Введите имя')
    age = forms.IntegerField(
        min_value=2,
        max_value=100,
        initial=18, help_text='Введите свой возраст')
    reklama = forms.BooleanField(label='Согласны получать рекламу?', required=False)
