from django.db import models
# Create your models here.

class Patient(models.Model):
    Statu = (('Fait','Fait'),
              ('En cours','En cours'),
              )

    T_A = (('Glycémie','Glycémie'),('Globules rouges','Globules rouges'),('Gaz du sang','Gaz du sang'),
           ('Cortisol','Cortisol'),('Insuline','Insuline'),
           ('Magnésium','Magnésium'),('Sodium','Sodium'),
           ('Uricémie','Uricémie'),('VIH','VIH'),
           ('Vitamine C','Vitamine C'),
           ("VGM : l'analyse du Volume Globulaire Moyen","VGM : l'analyse du Volume Globulaire Moyen"))

    ser = (('immunologie','immunologie'),
           ('cardiologie','cardiologie'),('radiologie','radiologie'),
           ('chirurgie','chirurgie'),('pneumologie','pneumologie'),
           ('dermatologie','dermatologie'),
           ('Pédiatrie','Pédiatrie'),
           ('traumatologie','traumatologie'),('maternité','maternité'),
           ('pneumologie','pneumologie'),
           ("service d'accueil de traitement des urgences","service d'accueil de traitement des urgences"))

    codebr = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=300,null=True)
    Prenom = models.CharField(max_length=300,null=True)
    services = models.CharField(max_length=300,null=True,choices=ser)
    Type_analyse = models.CharField(max_length=300,null=True,choices=T_A)
    Status = models.CharField(max_length=300,null=True,choices=Statu)
    date_creation= models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codebr
