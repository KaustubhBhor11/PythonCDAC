
# Create your views here.
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.utils.timezone import now, timedelta
from django.contrib import messages
from .models import User, OTPValidation
import random
from pymongo import MongoClient
from django.conf import settings

# MongoDB setup
client = MongoClient(settings.MONGO_URI)  # Use the MONGO_URI from settings.py
db = client[settings.MONGO_DB_NAME]  # Use the MONGO_DB_NAME from settings.py
collection = db['user_data']  # Replace with your MongoDB collection name



# Create your views here.
def signup(request):
    return render(request,'signup.html')

def OTP(request):
    return render(request,'OTP.html')

def fitness_attributes(request):
    return render(request,'fitness_attributes.html')


def signup_view(request):
    print('here')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            return redirect('/signup')

        user = User(username=username, email=email, password=password)
        user.save()
        print(f"User {user.username} added successfully!")

        otp = str(random.randint(100000, 999999))  
        otp_record = OTPValidation(email=email, otp=otp)
        otp_record.save()
        print(f"OTP for {otp_record.email} added successfully!")

        request.session['signup_data'] = {
            'username': username,
            'email': email,
            'password': password,
        }
        return redirect('/signup/otp/')

    return render(request, 'OTP.html')

def validate_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        email = request.session.get('signup_data', {}).get('email')

        try:
            otp_record = OTPValidation.objects.get(email=email, otp=otp)

            if now() - otp_record.created_time > timedelta(minutes=10):
                return redirect('/signup/otp/')

            return redirect('/signup/fitness_attributes/')

        except OTPValidation.DoesNotExist:
            return redirect('/signup/otp')

    return render(request, 'OTP.html')

def get_fitness_attributes(request):
    if request.method == 'POST':
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        activity = request.POST.get('activity')
        diseases = request.POST.get('diseases')

        email = request.session.get('signup_data', {}).get('email')

        if not email:
            return redirect('/signup/')

        try:
            user = User.objects.get(email=email)
            fitness_data = {
                'username': user.username,
                'email': user.email,
                'created_time': now(),
            }

            if weight:
                fitness_data['weight'] = weight
            if height:
                fitness_data['height'] = height
            if age:
                fitness_data['age'] = age
            if gender:
                fitness_data['gender'] = gender
            if activity:
                fitness_data['activity'] = activity
            if diseases:
                fitness_data['diseases'] = diseases
            collection.insert_one(fitness_data)

            return redirect('/home/')

        except User.DoesNotExist:
            return redirect('/signup/')

        except Exception as e:
            return redirect('/signup/fitness_attributes/')

    # If the request method is not POST, render the fitness attributes form
    return render(request, 'fitness_attributes.html')