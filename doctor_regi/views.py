from django.shortcuts import render
from .models import Doctor
import os

def doc_list(request):
    query = request.GET.get('search')
    doctors = Doctor.objects.all()

    if query:
        doctors = doctors.filter(name__icontains=query) | doctors.filter(address__icontains=query) 

    context = {
        'doctors': doctors,
        'title': 'Doctors List'
    }

    return render(request, 'doctor_regi/doc_list.html', context)

def doc_result(request):
    search_query = request.GET.get('search')
    doctors = Doctor.objects.filter(name__icontains=search_query)
    return render(request, 'doctor_regi/doc_result.html',{
        'doctors': doctors,
        'title' : f'Results for {search_query}' 
        })

def doc_regi(request):
    return render(request, 'doctor_regi/doc_page.html', {
        'title': 'Doctor Registration'
    })

def doc_loc(request):
    return render(request, 'doctor_regi/doc_map.html', { 
        'token' : os.environ.get('MAPPLES_TOKEN'),
        'title' : 'Maps',
    })