# Generated by Django 3.1.5 on 2021-03-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulaire', '0004_auto_20210311_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='codebr',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]
