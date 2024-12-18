from django.shortcuts import render
from django.http import JsonResponse
from .models import Example

def hello_mundo(request):
    examples = Example.objects.all()
    example_list = list(examples.values('id', 'name'))
    return JsonResponse(
        {
            "message":"sou felizzzzz",
            "examples" : example_list
        }
    )