import re
from django.core.validators import validate_email
from django.db.models import Q
from api import models

def is_email(email:str) -> bool:
    """Checks if an email is valid"""
    
    try:
        validate_email(email)
        return True
    except:
        return False


def is_phonenumber(phonenumber:str) -> bool:
    """Checks if phone number belongs to Côte d'Ivoire"""
    return True if re.fullmatch("\d{2}([- ]?\d{2}){4}", phonenumber) else False

def already_exists(email:str, phonenumber:str) -> bool:
    """Checks if a person has already email or phonenumber is registered"""
    
    person = models.PersonneAffiliee.objects.filter(Q(user__email=email) | Q(telephone_personneaffiliee=phonenumber))
    return True if person else False