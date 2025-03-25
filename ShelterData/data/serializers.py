from rest_framework import serializers

from .models import Medical_Facility, Resource, Shelter, Medical_facility_avalability, Resource_avalability, Victim, Missing_Person


class Medical_FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical_Facility
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class ShelterSerializer(serializers.ModelSerializer):
    # medical_facilities_available = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Medical_Facility.objects.all()
    # )
    # resources_available = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Resource.objects.all()
    # )

    # space_remaining = serializers.SerializerMethodField('get_space_remaining')
    class Meta:
        model = Shelter
        fields = ['id','name', 'location', 'isFull', 'space_remaining', 'resources_available', 'medical_facilities_available', 'max_capacity', 'members_in_shelter', 'latitude', 'longitude']
        depth = 3
    

    def get_space_remaining(self, obj):
        return obj.max_capacity-obj.members_in_shelter
    
    def validate(self, data):
        # Ensure members_in_shelter doesn't exceed max_capacity
        if data['members_in_shelter'] > data['max_capacity']:
            raise serializers.ValidationError("Members in shelter cannot exceed max capacity.")
        return data
    
class Missing_PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Missing_Person
        fields = ['name' , 'age', 'gender', 'health_condition', 'person_contact_number', 'person_to_contact', 'last_known_location', 'aadhaar_number']

class VictimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = '__all__' 

class VictimDetailsSerializer(serializers.Serializer):
    medical_facilities_names = serializers.ListField()
    resources_names = serializers.ListField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    