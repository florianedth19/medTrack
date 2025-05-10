from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser



# Create your models here.

# Model for the user
class User(AbstractUser): # pour etendre le model User de Django
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    first_name = models.CharField("Prénom", max_length=150, unique=False)
    last_name = models.CharField("Nom", max_length=150, unique=False)
    email = models.EmailField("Adresse email", unique=True) 
    role = models.CharField(max_length=50, default='patient', choices=[('patient', 'Patient'), ('medecin', 'Medecin'), ('aidant', 'Aidant')])

    USERNAME_FIELD = 'email'  # Django utilisera email comme identifiant
    REQUIRED_FIELDS = ['first_name', 'last_name']  
    
# Model for the profil medical

class ProfilMedical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil_medical')
    maladies_chroniques= models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medecin_traitant = models.TextField(max_length=150, blank=True, null=True)
    historique = models.TextField(blank=True, null=True)

# Model for planification
class Planification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planifications')
    medicament = models.CharField(max_length=150,blank=True, null=True)
    debut_traitement = models.DateField()
    fin_traitement = models.DateField()
    heure_prise = models.TimeField()
    date_fin = models.DateField()
    heure = models.TimeField()
    dose = models.CharField(max_length=150)
    frequence = models.CharField(max_length=150, blank=True, null=True, choices=[('quotidien', 'Quotidien'), ('hebdomadaire', 'Hebdomadaire'), ('mensuel', 'Mensuel')])

# Model for historiquePrise
class HistoriquePrise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    planification_id = models.ForeignKey(Planification, on_delete=models.CASCADE, related_name='historiques')
    date_prise = models.DateField()
    heure_prise = models.TimeField()
    prise = models.BooleanField(default=False)

# Model for notification
class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    date_envoi = models.DateField()
    heure_envoi = models.TimeField()
    lu = models.BooleanField(default=False)

# Model for rapport
class Rapport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rapports')
    date = models.DateField()
    heure = models.TimeField()
    message = models.TextField()
    lu = models.BooleanField(default=False)

# Model for indicateur
class IndicateurSuivi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="indicateurs")
    date = models.DateField()
    glycemie = models.FloatField()
    pression_systolique = models.IntegerField()
    pression_diastolique = models.IntegerField()
    poids = models.FloatField()
    taille = models.FloatField()

    def __str__(self):
        return f"Indicateur de {self.user.username} - {self.date}"

# Model for medicament
class Medicament(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medicaments')
    nom = models.CharField(max_length=150)
    heure_prise = models.TimeField(default="00:00")
    dosage = models.CharField(max_length=150, blank=True, null=True)
    commentaire = models.TextField(blank=True, null=True)
    pris = models.BooleanField(default=False)  # Nouveau champ booléen