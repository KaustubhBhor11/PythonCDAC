from signup import views
from django.urls import path


urlpatterns=[
    path('',views.signup),
    path('otp/',views.OTP),
    path('validate_otp/',views.validate_otp),
    path('signup_view/',views.signup_view),
    path('fitness_attributes/',views.fitness_attributes),
    path('get_attributes/',views.get_fitness_attributes),
]