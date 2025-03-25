from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics

from .models import Medical_Facility, Resource, Shelter
from .serializers import Medical_FacilitySerializer, ResourceSerializer, ShelterSerializer, VictimSerializer, Missing_PersonSerializer, VictimDetailsSerializer
from rest_framework import status
from .decorators import method_permission_classes
from .helper import get_similar_victims, get_best_shelter, check_among_missing_persons

# Create your views here.


class MedicalFacilityListView(APIView):
    
    serializer_class = Medical_FacilitySerializer
    def get(self, request):
        queryset = Medical_Facility.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class ResourceListView(APIView):
    serializer_class = ResourceSerializer
    def get(self, request):
        queryset = Resource.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
        

class ShelterListView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ShelterSerializer
    def get(self, request):
        queryset = Shelter.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    



class ShelterPostView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ShelterSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ShelterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        # Ensure only authenticated users can update
        serializer.save()
    
class BestShelterView(APIView):
    def post(self, request, top=1):
        serializer = VictimDetailsSerializer(data = request.data)
        if serializer.is_valid():
            shelters = get_best_shelter(request.data, top=top)
            if(len(shelters)):
                if top==1:
                    shelters_serializer = ShelterSerializer(shelters[0])
                else:
                    shelters_serializer = ShelterSerializer(shelters, many=True)
                    print(shelters_serializer.data)
                return Response(shelters_serializer.data, status=status.HTTP_200_OK)
            return Response(None, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
        
        
class VictimPostView(APIView):
    
    serializer_class = VictimSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            victim = serializer.save()
            matched_missing_persons = check_among_missing_persons(victim)
            if (len(matched_missing_persons)):
                
                if (len(matched_missing_persons)==1):
                    mmp_serializer = Missing_PersonSerializer(matched_missing_persons[0])
                elif (len(matched_missing_persons)>1):
                    mmp_serializer = Missing_PersonSerializer(matched_missing_persons, many=True)
                return Response(mmp_serializer.data, status=status.HTTP_200_OK)
            return Response(None, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MissingPersonView(APIView):
    serializer_class = Missing_PersonSerializer


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            missing_person = serializer.save()
            similar_victims = get_similar_victims(missing_person)
            sv_serializer = VictimSerializer(similar_victims, many=True)
            return Response(sv_serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



