from django.db import models
from django.db.models import CheckConstraint, Q, F
# Create your models here.



gender_choices = [('M', 'male'), ('F', 'Female')]

class Resource(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name

class Medical_Facility(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    


class Shelter(models.Model):
    name = models.CharField(max_length=300)
    location = models.TextField()
    max_capacity = models.PositiveIntegerField()
    members_in_shelter = models.PositiveIntegerField()
    space_remaining = models.PositiveIntegerField(default=0)
    isFull = models.BooleanField(default=False)
    medical_facilities_available = models.ManyToManyField(Medical_Facility, through='Medical_facility_avalability', blank=True)
    resources_available = models.ManyToManyField(Resource, through='Resource_avalability', blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(max_capacity__gte = F('members_in_shelter')), 
                name = 'check_members_in_shelter',
            ),
        ]


    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        # Automatically update space_remaining and isFull
        self.space_remaining = self.max_capacity - self.members_in_shelter
        self.isFull = self.space_remaining <= 0
        super().save(*args, **kwargs)
    

    
# class PhoneNumber(models.Model):
#     pass
unit_choices = [('kg', 'kg'),
                ('ltr', 'ltr'),
                ('item', 'item')]
class Resource_avalability(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(choices=unit_choices, max_length=50, default='item')
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, default=None)

class Medical_facility_avalability(models.Model):
    medical_facility = models.ForeignKey(Medical_Facility, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(choices=unit_choices, max_length=50, default='item')
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, default=None)

class Victim(models.Model):

    
    name = models.CharField(max_length=300)
    age  = models.PositiveIntegerField()
    gender = models.CharField(max_length=50, choices=gender_choices)
    health_condition = models.TextField()
    personal_number = models.CharField(max_length=20, null=True, blank=True)
    emergency_contact = models.CharField(max_length=20, null=True, blank=True)
    shelter_registered = models.ForeignKey(Shelter, on_delete=models.SET_NULL, null=True)
    aadhaar_number = models.CharField(max_length=12, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name


class Missing_Person(models.Model):
    name = models.CharField(max_length=300)
    age  = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=gender_choices)
    health_condition = models.TextField(null=True, blank=True)
    person_contact_number = models.CharField(max_length=20, null=True, blank=True)
    person_to_contact = models.CharField(max_length=20)
    last_known_location = models.TextField(null=True, blank=True)
    aadhaar_number = models.CharField(max_length=12, null=True, blank=True)
    found = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name



