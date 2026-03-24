from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(label="Имя пользователя",)
    age = forms.IntegerField(label="Введите возраст")
