from django.shortcuts import render
from pymongo import MongoClient
import os

def home(request):
    return render(request, 'ndapp/home.html',{
        'title': 'Home'
    })

def services(request):
    return render(request, 'ndapp/services.html', {
        'title': 'Services'
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Connect to MongoDB
        client = MongoClient(os.environ.get('MONGO_URI'))
        db = client['remedies']
        collection = db['contact_requests']

        # Insert user data into MongoDB
        user_data = {
            'name': name,
            'email': email,
            'message': message
        }
        collection.insert_one(user_data)

        return render(request, 'ndapp/formsubmit.html', {
            'title': 'Form Submitted'
        })

    return render(request, 'ndapp/contact.html', {
        'title': 'Contacts'
    })

def emergencies(requests):
    return render(requests, 'ndapp/emergencies.html',{
        'title': 'Emergency Guidelines'
    })

def medicalNews(requests):
    return render(requests, 'ndapp/medicalnews.html',{
        'title': 'Medical News'
    })

def healthtopics(requests):
    return render(requests, 'ndapp/healthtopics.html',{
        'title': 'Health Topics'
    })

def termsandconditions(requests):
    return render(requests, 'ndapp/tandc.html',{
        'title': 'Terms and Conditions'
    })

def privacypolicy(requests):
    return render(requests, 'ndapp/pp.html',{
        'title': 'Privacy Policy'
    })
def ec(requests):
    return render(requests, 'ndapp/emhl.html',{
        'title': 'Emergency Helplines'
    })