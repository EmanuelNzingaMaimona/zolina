from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from json import load

MUNICIPE_CHOICES=[]

def fill_p():
    PROVINCE_CHOICES=[]
    with open('client/static/provincias-cidades.json') as f:
        data = load(f)
        for t in data:
            PROVINCE_CHOICES.append(tuple((t['name'], t['name'])))
        PROVINCE_CHOICES = tuple(PROVINCE_CHOICES) 
    return PROVINCE_CHOICES

GROUP_CHOICES = (
    ('A+','A+'),
    ('AB+', 'AB+'),
    ('B+','B+'),
    ('O+','O+'),
    ('A-','A-'),
    ('AB-', 'AB-'),
    ('B-','B-'),
    ('O-','O-'),
)
PROVINCE_CHOICES=fill_p()
# Create your models here.
class Message(models.Model):
    dest = models.CharField(max_length=9)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # send(body='kkkk',to='947221912')
        return super().save(*args, **kwargs)
    
class Donor(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=13)
    district = models.CharField(max_length=150)
    group = models.CharField(max_length=50, choices=GROUP_CHOICES, default="A+")
    province = models.CharField(max_length=50, choices=PROVINCE_CHOICES, default="Bengo")
    municipe = models.CharField(max_length=100)
    picture = models.ImageField(blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name
