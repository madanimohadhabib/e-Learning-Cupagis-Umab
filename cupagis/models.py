from django.db import models
from django.contrib.auth.models import User



class Module(models.Model):
    niveau_LISTE= (
        ('M1','Master1'),
        ('M2','Master2'),
    )
    semestre_LISTE= (
        ('S1','semestre1'),
        ('S2','semestre2'),
    )
    nom_Module = models.CharField(max_length=255,verbose_name='nom de module')
    img = models.FileField(upload_to='module_images/')
    niveau = models.CharField(max_length=2,choices=niveau_LISTE)
    semestre = models.CharField(max_length=2,choices=semestre_LISTE)
    prof = models.ForeignKey(User, on_delete=models.CASCADE,related_name='module')
    date_Creation = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    
    def __str__(self):
            return self.nom_Module

class Cour(models.Model):
    module = models.ForeignKey(Module,verbose_name='nom de module', on_delete=models.SET)
    titre_Cour = models.CharField(max_length=255,verbose_name='titre cour')
    fichier_Cour = models.FileField(upload_to='cour_files/')  # Vous pouvez utiliser FileField pour les fichiers
    date_Creation = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    
    def __str__(self):
            return self.titre_Cour

class TP(models.Model):
    module = models.ForeignKey(Module,verbose_name='nom de module', on_delete=models.SET)
    titre_TP = models.CharField(max_length=255,verbose_name='titre tp')
    fichier_TP = models.FileField(upload_to='tp_files/')  # Vous pouvez utiliser FileField pour les fichiers
    date_Creation = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    
    def __str__(self):
            return self.titre_TP
