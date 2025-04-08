from django.shortcuts import render

# Create your views here.
# def profile(request):
#     return render(request,'profile.html')

from django.shortcuts import render, redirect
from django.conf import settings
from pymongo import MongoClient
from django.core.files.storage import FileSystemStorage
import os

# MongoDB setup
client = MongoClient(settings.MONGO_URI)  # Use the MONGO_URI from settings.py
db = client[settings.MONGO_DB_NAME]  # Use the MONGO_DB_NAME from settings.py
collection = db['user_data']  # Replace with your MongoDB collection name

def profile(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        activity = request.POST.get('activity')

        # Handle file upload
        profile_image = None
        if 'profile_image' in request.FILES:
            image_file = request.FILES['profile_image']
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'profile_images'))
            filename = fs.save(image_file.name, image_file)
            profile_image = fs.url(filename)

        # Build the profile data
        profile_data = {
            'username': username,
            'email': email,
            'weight': weight,
            'height': height,
            'age': age,
            'gender': gender,
            'activity': activity,
        }

        # Add the profile image URL if provided
        if profile_image:
            profile_data['profile_image'] = profile_image

        # Update the user's profile in MongoDB
        collection.update_one({'email': email}, {'$set': profile_data}, upsert=True)

        # Redirect to the profile page with a success message
        return redirect('/profile/')

    # For GET requests, render the profile page
    return render(request, 'profile.html')