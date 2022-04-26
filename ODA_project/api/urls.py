from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'api'

urlpatterns = [
    # path('', views.home, name='home'),
    path('v1/afficher_constante', views.afficher_constante, name='afficher_constante'),
    # path('v1/ajouter_constante', views.ajouter_constante, name='ajouter_constante'),
    # path('v1/inscription', views.inscription, name='inscription'),
    # path('v1/deconnexion', views.deconnexion, name='deconnexion'),
    # path('v1/connexion', views.connexion, name='connexion'),
    # path('v1/deconnexion', views.deconnexion, name='deconnexion'),
    # path('v1/personne_affiliee/<int:pk>', views.PersonneAffilieeAPIView.as_view(), name='personne_affiliee'),
    # path('v1/personne_vulnerable', views.PersonneVulnerablesAPIView.as_view(), name='ajouter_personne_vulnerable'),
    # path('v1/personne_vulnerable/<int:pk>', csrf_exempt(views.PersonneVulnerableAPIView.as_view()), name='supprimer_personne_vulnerable'),
    # path('v1/type_antecedent_medical', views.TypeAntecedentMedicalsAPIView.as_view(), name='ajouter_type_antecedent_medical'),
    # path('v1/type_antecedent_medical/<int:pk>', csrf_exempt(views.TypeAntecedentMedicalAPIView.as_view()), name='supprimer_type_antecedent_medical'),
    
    # path('v1/recuperer_temperature', views.recuperer_temperature, name='recuperer_temperature'),
    # path('v1/ajouter_enregistrement', views.ajouter_enregistrement, name='ajouter_enregistrement'),
    # path('v1/afficher_enregistrement', views.afficher_enregistrement, name='afficher_enregistrement'),
    # path('v1/supprimer_enregistrement', views.supprimer_enregistrement, name='supprimer_enregistrement'),


    path('v1/enregistrement_video', views.EnregistrementVideosAPIView.as_view(), name='ajouter_engregistrement'),
    path('enregistrement_video/<int:pk>', csrf_exempt(views.EnregistrementVideoAPIView.as_view()), name='modifier_enregistrement'),



]
    
