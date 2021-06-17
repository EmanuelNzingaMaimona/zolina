import django_filters
from .models import *

class DonorFilter(django_filters.FilterSet):
    class meta:
        model = Donor
        fields = '__all__'
