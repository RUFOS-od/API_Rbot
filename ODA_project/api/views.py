# from genericpath import exists
# from re import T
# from typing_extensions import dataclass_transform
# from django.shortcuts import render
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
# from rest_framework.views import APIView
from asyncio import streams
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from managers import managers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import ConstantesSerializers, EnregistrementVideoSerializers
from .models import Constantes, EnregistrementVideo,PersonneVulnerable
# # Create your views here.

# @api_view(['GET'])
# def home(request):
#     return Response({'message': "Bienvenue sur l'API de RBot !"})

@api_view(['GET'])
def afficher_constante(request):
    constante= Constantes.objects.all().order_by('-id_constantes')[:1]
    serializer= ConstantesSerializers(constante,many=True)
    return Response(serializer.data)

# @swagger_auto_schema(methods=['POST'], responses={201:openapi.Response('Inscription bien éffectuée !')}, operation_description="Inscription d'une personne affiliée", request_body=PersonneAffilieeSerializer)
# @api_view(['POST'])
# def inscription(request):
#     message = ''
#     success = False
#     if request.method == 'POST':
#         data = request.data
        
#         if not data.get('nom') or data.get('nom').isspace() or data.get('prenoms').isspace() or not data.get('tel') or data.get('tel').isspace() or not data.get('email') or data.get('email').isspace() or not data.get('pwd1') or data.get('pwd1').isspace() or not data.get('pwd2') or data.get('pwd2').isspace():
#             message = 'Veuillez remplis les champs requis !'
#         elif not managers.is_email(email=data.get('email')):
#             message = 'Veuillez saisir un email valide !'
#         elif not managers.is_phonenumber(phonenumber=data.get('tel')):
#             message = 'Veuillez saisir un numéro de téléphone au format XX-XX-XX-XX-XX ou XXXXXXXXXX'
#         elif managers.already_exists(email=data.get('email'), phonenumber=data.get('tel')):
#             message = 'Personne existante déjà avec email ou numéro de téléphone'
#         elif len(data.get('pwd1')) < 8:
#             message = "Veuillez saisir un mot de passe d'au moins 8 caractères"
#         elif data.get('pwd1') != data.get('pwd2'):
#             message = 'Les mots de passe ne sont pas identiques'
#         else:
#             user = get_user_model().objects.create(
#                 last_name=data.get('nom'),
#                 first_name=data.get('prenoms'),
#                 email=data.get('email')
#             )
#             user.set_password(data.get('pwd1'))
#             user.save()
            
#             person = PersonneAffiliee(
#                 user=user,
#                 telephone_personneaffiliee=data.get('tel')
#             )
            
#             person.save()
#             message = 'Personne affiliée bien ajoutée !'
#             success = True
            
#         return Response({'message':message, 'success':success})



# @api_view(['POST'])
# def connexion(request):
#     data = request.data
#     message = ''
#     success = False
    
#     if not data.get('email') or data.get('email').isspace() or not data.get('password') or data.get('password').isspace():
#         message = 'Veuillez remplir les champs requis !'
#     else:
#         user = authenticate(request, email=data.get('email'), password=data.get('password'))
        
#         if user:
#             login(request, user)
#             message = 'Connexion réussie !'
#             success = True
#         else:
#             message = 'Email ou mot de passe incorrect !'
    
#     return Response({'message':message, 'success':success})


# @api_view(['GET'])
# def deconnexion(request):
#     logout(request)
    
#     return Response({'message':'Vous êtes déconnecté(e) !', 'success':True})


# @api_view(['POST'])
# def ajouter_constante(request):
#     data=request.data
#     temperature = data.get('temperature')
#     date_constantes = data.get('date_constantes')
#     id_personnevulnerable  = data.get('id_personnevulnerable')
#     personnevulnerable = PersonneVulnerable.objects.get(pk=id_personnevulnerable)

#     constante = Constantes(
#         temperature=temperature, 
#         date_constantes=date_constantes, 
#         personnevulnerable=personnevulnerable
#         )
#     constante.save()

#     return Response({'message': 'Constante bien ajoutée !'})

# class PersonneVulnerablesAPIView(APIView): 
#     def get(self, request):
#         """affichage d'une personne vulnerable"""
#         personne_vulnerable= PersonneVulnerable.objects.all()
#         serializer= PersonneVulnerableSerializers(personne_vulnerable,many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         """ajout d'une personne vulnerable"""
#         data=request.data
#         nom_personne_vulnerable = data.get('nom_personne_vulnerable')
#         numero_telephone_personne_vulnerable = data.get('numero_telephone_personne_vulnerable')
#         picture  = data.get('picture')
#         photo_nom = data.get('photo_nom')
#         age  = data.get(' age')
#         prenoms_personne_vulnerable = data.get('prenoms_personne_vulnerable')

#         personnevulnerable = PersonneVulnerable(
#             nom_personne_vulnerable=nom_personne_vulnerable, 
#             numero_telephone_personne_vulnerable=numero_telephone_personne_vulnerable, 
#             picture=picture,
#             photo_nom=photo_nom,
#             age=age,
#             prenoms_personne_vulnerable=prenoms_personne_vulnerable
#             )
#         personnevulnerable.save()

#         return Response({'message': 'Personne bien ajoutée !'})

# class PersonneVulnerableAPIView(APIView): 
#     def delete(self,request,pk):
#         personne = PersonneVulnerable.objects.get(id_personne_vulnerable=pk)
#         personne.delete()
#         return Response({'message': 'Personne supprimée avec succès !'})
    
#     def put(self, request,pk):
#         try:
#             personne=PersonneVulnerable.objects.get(id_personne_vulnerable=pk)
#             serializer = PersonneVulnerableSerializers(personne, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response({'message': "personne vulnerable inconnue"})

# class TypeAntecedentMedicalsAPIView(APIView): 
#     def get(self, request):
#         """affichage d'un type antecedent medical"""
#         type_antecedent_medical= TypeAntecedentMedical.objects.all()
#         serializer= TypeAntecedentMedicalSerializers(type_antecedent_medical,many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         """ajout d'un type_antecedent_medical"""
#         data=request.data
#         nom_type_antecedent_medical = data.get('nom_type_antecedent_medical')

# class PersonneAffilieeAPIView(APIView):
#     def get(self, request, pk):
#         try:
#             person = PersonneAffiliee.objects.get(id_personneaffilliee=pk)
#             serializer = PersonneAffilieeSerializer(person)
            
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except:
#             return Response({'message':'Personne affiliée inconnue !'})
    
#     def put(self, request, pk):
#         data = request.data
#         try:
#             person = PersonneAffiliee.objects.get(id_personneaffilliee=pk)
#             if not data.get('nom') or data.get('nom').isspace() or not data.get('prenoms') or data.get('prenoms').isspace() or not data.get('tel') or data.get('tel').isspace():
#                 return Response({'message': 'Veuillez remplir les champs requis !'})
#             elif not managers.is_phonenumber(phonenumber=data.get('tel')):
#                 message = 'Veuillez saisir un numéro de téléphone au format XX-XX-XX-XX-XX ou XXXXXXXXXX'
#             else:
#                 person.user.last_name = data.get('nom')
#                 person.user.first_name = data.get('prenoms')
#                 person.user.save()
                
#                 person.telephone_personneaffiliee = data.get('tel')
#                 person.save()

#             return Response({'message':'Personne affiliée bien modifiée !'}, status=status.HTTP_200_OK)
#         except:
#             return Response({'message':'Personne affiliée inconnue !'})
    
#     def delete(self, request, pk):
#         try:
#             person = PersonneAffiliee.objects.get(id_personneaffilliee=pk)
#             person.delete()
#             return Response({'message':'Personne affiliée bien supprimée !'}, status=status.HTTP_200_OK)
#         except:
#             return Response({'message':'Personne affiliée inconnue !'})
#         type_antecedent_medical = TypeAntecedentMedical(
#             nom_type_antecedent_medical=nom_type_antecedent_medical, 
#             )
#         type_antecedent_medical.save()

#         return Response({'message': 'Type antecedent medical bien ajoutée !'})

# class TypeAntecedentMedicalAPIView(APIView): 
#     def delete(self,request,pk):
#         type_antecedent_medical = TypeAntecedentMedical.objects.get(id_type_antecedent_medical=pk)
#         type_antecedent_medical.delete()
#         return Response({'message': 'Type antecedent medical supprimée avec succès !'})
    
#     def put(self, request,pk):
#         try:
#             type_antecedent_medical=TypeAntecedentMedical.objects.get(id_type_antecedent_medical=pk)
#             serializer = TypeAntecedentMedicalSerializers(type_antecedent_medical, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             return Response({'message': "type antecedent medical inconnue"})


# @api_view(['GET'])
# def recuperer_temperature(request,):
#     antecedent=AntecedentMedical.objects.get(id_antecedent_medical=1)
#     constante= Constantes.objects.all().order_by('-id_constante')[:1]
#     temperature_prise=constante.temperature
#     temperature_normale=antecedent.temperature_normale
#     if temperature_prise != temperature_normale:
#         return Response({'message': "on doit créer un programme pour alerter les parents "})
#     else:
#         return Response({'message': "la temperature est normale"})


@api_view(['POST'])
def ajouter_enregistrement(request):
    data=request.data
    heure_debut = data.get('heure_debut')
    heure_fin = data.get('heure_fin')
    #data_enregistrement=data.get('data_enregistrement')
   # piece = data.get('piece')
    #id_personne_affiliee  = data.get('id_personne_affiliee')
   # personne_affiliee = PersonneVulnerable.objects.get(pk=id_personne_affiliee)

    # enregistrement = EnregistrementVideo(
    #     heure_debut=heure_debut, 
    #     heure_fin=heure_fin,
        #id_personne_affiliee = id_personne_affiliee,
        #data_enregistrement = data_enregistrement,
        #piece =piece,
        #personne_affiliee=personne_affiliee
    #     )
    # enregistrement.save()

    # return Response({'message': 'Programmation pour votre enregistrement est éffectuer avec succes!'})




# @api_view(['GET'])
# def afficher_enregistrement(request):
#     enregistrement= EnregistrementVideo.objects.all()
#     serializer= EnregistrementVideoSerializers(enregistrement,many=True)
#     return Response(serializer.data)



# @api_view(['DELETE'])
# def supprimer_enregistrement(request,pk):
#     enregistrement = EnregistrementVideo.objects.get(id_enregistrement_video=pk)
#     serializer= EnregistrementVideoSerializers(enregistrement,many=True)
#     enregistrement.delete()
#     return Response(serializer.data)

    #return Response({'message': 'Vidéo supprimée avec succès !'})
 







class EnregistrementVideosAPIView(APIView): 
    def get(self, request):
        """affichage d'une personne vulnerable"""
        enregistrement= EnregistrementVideo.objects.all()
        serializer= EnregistrementVideoSerializers(enregistrement,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """ajout d'une personne vulnerable"""
        data=request.data
        heure_debut = data.get('heure_debut')
        heure_fin = data.get('heure_fin')
        

        enregistrement = EnregistrementVideo(
            heure_debut=heure_debut, 
            heure_fin=heure_fin, 
            
            )
        enregistrement.save()

        return Response({'message': 'Video bien programmée !'})

class EnregistrementVideoAPIView(APIView): 
    def delete(self,request,pk):
        heure_debut = EnregistrementVideo.objects.get(heure_debut=pk)
        heure_debut.delete()
        return Response({'message': 'video bien supprimée !'})
    
    def put(self, request,pk):
        try:
            heure_debut=EnregistrementVideo.objects.get(heure_debut=pk)
            serializer = EnregistrementVideoSerializers(heure_debut, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': "Video non trouvable"})
