from importlib.metadata import requires

from django.shortcuts import render
from .forms import PersonForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Person

# Получение данных из БД
def index(request):
    person = PersonForm()
    people = Person.objects.all()
    return render(request, 'index.html', {'form': form, 'people': people})



# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get('name')
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect('/')

# Изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'edit.html', {'person': person})

# Удаление данных из БД
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

    person.delete()
    return HttpResponseRedirect('/')