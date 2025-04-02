from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.decorators import action



# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get("email")
        if User.objects.filter(email=email).exists():
            return Response({"error": "Cet email est déjà utilisé."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(
            first_name=request.data.get('first_name', ''),
            last_name=request.data.get('last_name', '')
        )
            return Response({"message": "Utilisateur créé avec succès"}, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], url_path="login")
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class ProfilMedicalViewSet(viewsets.ModelViewSet):
    queryset = ProfilMedical.objects.all()
    serializer_class = ProfilMedicalSerializer

class PlanificationViewSet(viewsets.ModelViewSet):
    queryset = Planification.objects.all()
    serializer_class = PlanificationSerializer

class HistoriquePriseViewSet(viewsets.ModelViewSet):
    queryset = HistoriquePrise.objects.all()
    serializer_class = HistoriquePriseSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class RapportViewSet(viewsets.ModelViewSet):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer

class IndicateurSanteViewSet(viewsets.ModelViewSet):
    queryset = IndicateurSante.objects.all()
    serializer_class = IndicateurSanteSerializer