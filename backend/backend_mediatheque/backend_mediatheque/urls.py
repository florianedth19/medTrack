"""
URL configuration for backend_mediatheque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from mediatheque.views import *
#urlpatterns = [
    #path('admin/', admin.site.urls),
#]
router = DefaultRouter()
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profils', ProfilMedicalViewSet)
router.register(r'planifications', PlanificationViewSet)
router.register(r'historique', HistoriquePriseViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'rapports', RapportViewSet)
router.register(r'indicateurs', IndicateurSuiviViewSet)
router.register(r'medicaments', MedicamentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]