from django.contrib import admin


from .models import Medical_Facility, Resource, Shelter, Medical_facility_avalability, Resource_avalability, Victim, Missing_Person
# Register your models here.
admin.site.register(Medical_Facility)
admin.site.register(Resource)
admin.site.register(Shelter)
admin.site.register(Medical_facility_avalability)
admin.site.register(Resource_avalability)
admin.site.register(Victim)
admin.site.register(Missing_Person)