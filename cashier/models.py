from django.db import models
from django.contrib.auth.models import User

DESIGNATION = ( 
    ('Cashier', 'Cashier'),
    ('Manager','Manager'),
    ('Accountant','Accountant'),
)

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    position = models.CharField(max_length=100, choices=DESIGNATION, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to ='profile_images')

    def __str__(self):
        return f'{self.staff.username}-Profile'
