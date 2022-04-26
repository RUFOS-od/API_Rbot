# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth import get_user_model



class PersonneaffilieRobot(models.Model):
    id_personne_affiliee = models.ForeignKey('PersonneAffiliee', models.DO_NOTHING, db_column='id_personne_affiliee', blank=True, null=True)
    id_robot = models.ForeignKey('Robot', models.DO_NOTHING, db_column='id_robot', blank=True, null=True)
    temps = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'PersonneAffilie_Robot'


class AntecedentMedical(models.Model):
    id_antecedent_medical = models.AutoField(primary_key=True)
    libelle_antecedent_medical = models.CharField(max_length=50, blank=True, null=True)
    id_type_antecedent_medical = models.ForeignKey('TypeAntecedentMedical', models.DO_NOTHING, db_column='id_type_antecedent_medical', blank=True, null=True)
    id_personne_vulnerable = models.ForeignKey('PersonneVulnerable', models.DO_NOTHING, db_column='id_personne_vulnerable', blank=True, null=True)

    class Meta:
        db_table = 'antecedent_medical'


class Constantes(models.Model):
    id_constantes = models.AutoField(primary_key=True)
    temperature = models.CharField(max_length=30, blank=True, null=True)
    tension = models.CharField(max_length=30, blank=True, null=True)
    temps_de_prise = models.DateTimeField(blank=True, null=True)
    id_personne_vulnerable = models.ForeignKey('PersonneVulnerable', models.DO_NOTHING, db_column='id_personne_vulnerable', blank=True, null=True)

    class Meta:
        db_table = 'constantes'


class EnregistrementVideo(models.Model):
    id_enregistrement_video = models.AutoField(primary_key=True)
    heure_debut = models.DateTimeField(blank=True, null=True)
    heure_fin = models.DateTimeField(blank=True, null=True)
    data_enregistrement = models.DateField(blank=True, null=True)
    piece = models.CharField(max_length=40, blank=True, null=True)
    id_personne_affiliee = models.ForeignKey('PersonneAffiliee', models.DO_NOTHING, db_column='id_personne_affiliee', blank=True, null=True)

    class Meta:
        db_table = 'enregistrement_video'


class PersonneAffiliee(models.Model):
    id_personne_affiliee = models.AutoField(primary_key=True)
    type_personne_affiliee = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'personne_affiliee'


class PersonneVulnerable(models.Model):
    id_personne_vulnerable = models.AutoField(primary_key=True)
    nom_personne_vulnerable = models.CharField(max_length=50, blank=True, null=True)
    prenom_personne_vulnerable = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    telephone = models.CharField(max_length=16, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)
    temperature_normale = models.CharField(max_length=30, blank=True, null=True)
    images_personne_vulnerable = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'personne_vulnerable'


class Robot(models.Model):
    id_robot = models.AutoField(primary_key=True)
    nom_robot = models.CharField(max_length=50, blank=True, null=True)
    adresse_ip = models.CharField(max_length=30, blank=False, null=True)
    id_personne_vulnerable = models.ForeignKey(PersonneVulnerable, models.DO_NOTHING, db_column='id_personne_vulnerable', blank=True, null=True)

    class Meta:
        db_table = 'robot'


class TypeAntecedentMedical(models.Model):
    id_type_antecedent_medical = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'type_antecedent_medical'
