from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class Startup(models.Model):
    StartupName=models.CharField(max_length=50)
    FIRM_CHOICES = [
        ('Tech', 'Technology'),
        ('FinTech','Financial technology'),
        ('Marketing', 'Marketing'),
        ('Design', 'Design'),

        # Add more choices as needed
    ]
    firm = models.CharField(max_length=10, choices=FIRM_CHOICES)
    Description=models.CharField(max_length=50)
    Address=models.CharField(max_length=20)
    email= models.EmailField(max_length=30)
    socialmedialink=models.URLField(max_length=30, )
    Funding_Status=models.TextField(max_length=20,)
    logo=models.ImageField(upload_to='images')

    def __str__(self):
        return self.StartupName

    