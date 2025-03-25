
from .models import Shelter, Missing_Person, Victim
from django.db.models import Case, When, IntegerField, Value, F, Q, Sum, ExpressionWrapper, FloatField
import math



def search_missing_person(missing_person):
    
    query = Q(Q(name__icontains = missing_person.name))
    if missing_person.age>0:
       query|= Q(Q(age__lte = missing_person.age+5) & Q(age__gte= missing_person.age-5))

def get_similar_victims(missing_person):
    filters = []
    
    
    filters.append(When(name__icontains=missing_person.name, then=Value(10)))
    if missing_person.age>0:
        filters.append(When(Q(Q(age__lte = missing_person.age+5) & Q(age__gte= missing_person.age-5)), then=Value(1)))
    if missing_person.person_contact_number:
        filters.append(When(personal_number = missing_person.person_contact_number, then=Value(100)))
    if missing_person.aadhaar_number:
        filters.append(When(aadhaar_number = missing_person.aadhaar_number, then=Value(100)))
    
    similarity_score = 0
    for filter in filters:
        similarity_score+= Sum(Case(filter, default=Value(0), output_field=IntegerField()))
        
    
    # Annotate with similarity score
    similar_victims = Victim.objects.annotate(
        similarity_score=similarity_score
    ).filter(similarity_score__gt=0, gender=missing_person.gender).order_by('-similarity_score')  # Sort by most similar

    print([sv.similarity_score  for sv in similar_victims])
    return similar_victims

def check_among_missing_persons(victim):
    filters = []
    
    
    filters.append(When(name__icontains=victim.name, then=Value(10)))
    if victim.age>0:
        filters.append(When(Q(Q(age__lte = victim.age+5) & Q(age__gte= victim.age-5)), then=Value(1)))
    if victim.personal_number:
        filters.append(When(person_contact_number = victim.personal_number, then=Value(100)))
    if victim.aadhaar_number:
        filters.append(When(aadhaar_number = victim.aadhaar_number, then=Value(100)))
    if victim.emergency_contact:
        filters.append(When(person_to_contact = victim.emergency_contact, then=Value(100)))
    similarity_score = 0
    for filter in filters:
        similarity_score+= Sum(Case(filter, default=Value(0), output_field=IntegerField()))
        
    
    # Annotate with similarity score
    mathced_missing_persons = Missing_Person.objects.annotate(
        similarity_score=similarity_score
    ).filter(similarity_score__gte=100, gender=victim.gender, found=False).order_by('-similarity_score')  # Sort by most similar

    
    return mathced_missing_persons



def get_best_shelter(victim_details, top=1):
    # R = 6371  # Earth's radius in km

    # lat1 = math.radians(victim_details['latitude'])
    # lon1 = math.radians(victim_details['longitude'])

    # lat2 = ExpressionWrapper(math.radians(F('latitude')), output_field=FloatField())
    # lon2 = ExpressionWrapper(math.radians(F('longitude')), output_field=FloatField())

    # dlat = ExpressionWrapper(lat2 - lat1, output_field=FloatField())
    # dlon = ExpressionWrapper(lon2 - lon1, output_field=FloatField())


    a = ExpressionWrapper(
        (F('latitude') - victim_details['latitude']) ** 2 + (F('longitude') - victim_details['longitude']) ** 2,
        output_field=FloatField()
    )  # Approximate distance squared (Euclidean-like for simplicity)

    query = Q()

    if len(victim_details['medical_facilities_names']):
        query|= Q(medical_facilities__name__in=victim_details['medical_facilities_names'])
    
    if len(victim_details['resources_names']):
        query|= Q(resources__name__in=victim_details['resources_names'])
    

    shelters = Shelter.objects.annotate(distance=a).filter(Q(Q(query) & Q(isFull=False))).distinct().order_by('distance')[:top]
    print(shelters)
    return shelters


    