from django.forms import ModelForm, CharField, IntegerField
from .models import Person


# Форма для создания и редактирования пользователя
class PersonForm(ModelForm):
    name = CharField(label="Имя пользователя",)
    age = IntegerField(label="Введите возраст")


    class Meta:
        model = Person
        fields = ['name', 'age']

