# Generated by Django 3.1.5 on 2021-03-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Nom',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Prenom',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Status',
            field=models.CharField(choices=[('Faite', 'Faite'), ('En cours', 'En cours'), ('Non disponible', 'Non disponible')], max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Type_analyse',
            field=models.CharField(choices=[('Glycémie', 'Glycémie'), ('Globules rouges', 'Globules rouges'), ('Gaz du sang', 'Gaz du sang'), ('Cortisol', 'Cortisol'), ('Insuline', 'Insuline'), ('Magnésium', 'Magnésium'), ('Sodium', 'Sodium'), ('Uricémie', 'Uricémie'), ('VIH', 'VIH'), ('Vitamine C', 'Vitamine C'), ("VGM : l'analyse du Volume Globulaire Moyen", "VGM : l'analyse du Volume Globulaire Moyen")], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='codebr',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='services',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
