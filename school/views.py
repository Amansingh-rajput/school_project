from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def test(request):
    return HttpResponse('test is working')


def school_list(request):
    school_list = School.objects.all()

    return render(request, 'school_list.html', {
        'school_list': school_list,
    })


def school_add(request):
    school_form = SchoolForm()

    if request.method == 'POST':
        school_form = SchoolForm(request.POST)
        if school_form.is_valid():
            school_form.save()
            return redirect('school_list')

    return render(request, 'school_add.html', {
        'school_form': school_form,
    })


def school_detail(request, school_id):
    school = School.objects.get(id=school_id)

    return render(request, 'school_detail.html', {
        'school': school,
    })


def school_edit(request, school_id):
    school = School.objects.get(id=school_id)
    school_form = SchoolForm(instance=school)

    if request.method == 'POST':
        school_form = SchoolForm(request.POST, instance=school)
        if school_form.is_valid():
            school_form.save()
            return redirect('school_list')

    return render(request, 'school_add.html', {
        'school_form': school_form,
    })

def school_delete(request, school_id):
    school = School.objects.get(id=school_id)
    school.delete()
    return redirect('school_list')