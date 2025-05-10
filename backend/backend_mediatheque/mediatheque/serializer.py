from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data['email'],
            role=validated_data.get('role', 'patient')
        )
        user.set_password(validated_data['password']) 
        user.save()

        #creation profil medical
        ProfilMedical.objects.create(user_id=user)
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("Email ou mot de passe incorrect")

        token, created = Token.objects.get_or_create(user=user)
        return {
            "token": token.key,
            "user": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "role": user.role
            }
        }

class ProfilMedicalSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)  #assure que user_id n'est pas modifiable
    maladies_chroniques = serializers.CharField(required=False)
    allergies = serializers.CharField(required=False)
    medecin_traitant = serializers.CharField(required=False)
    historique = serializers.CharField(required=False)

    class Meta:
        model = ProfilMedical
        fields = '__all__'

class PlanificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planification
        fields = '__all__'

class HistoriquePriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriquePrise
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = '__all__'

class IndicateurSuiviSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicateurSuivi
        fields = '__all__'

class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'