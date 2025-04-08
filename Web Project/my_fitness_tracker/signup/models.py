from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
import hashlib 

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Plain password
    encrypted_password = models.CharField(max_length=256)  # Encrypted password
    created_time = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        # Encrypt the password before saving
        self.encrypted_password = hashlib.sha256(self.password.encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'signup_user'

class OTPValidation(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_time = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.email} - {self.otp}"

    class Meta:
        db_table = 'signup_validation'