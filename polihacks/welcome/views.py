"""Welcome views"""

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Person

@login_required
def index(request):
    name = request.user.first_name
    return HttpResponse(f'Hola {name}, estás iniciado')

def add(request, numbers):
    numbers = numbers.split(',')
    numbers = [int(number) for number in numbers]
    result = 0
    for number in numbers:
        result += number
    return HttpResponse('El resultado es: ' + str(result))

def chat(request, name):
    persons = Person.objects.all()
    context = {
        'name': name,
        'persons': persons
    }
    return render(request, 'welcome/welcome.html', context=context)

def suma(request, age):
    return HttpResponse('La edad + 2 es ' + str(age + 2))