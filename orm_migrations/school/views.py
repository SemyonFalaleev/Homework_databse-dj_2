from django.views.generic import ListView
from django.shortcuts import render

from .models import Student

def students_list(request):
    template = 'school/students_list.html'  
    ordering = 'group'
    obj_dict = {k: list(k.teachers.all()) for k in Student.objects.order_by(ordering)}
    context = {
        'object_list': obj_dict.items(),
    }

    return render(request, template, context)
