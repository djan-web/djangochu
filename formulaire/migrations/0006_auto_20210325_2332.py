# Generated by Django 3.1.5 on 2021-03-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulaire', '0005_auto_20210312_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='codebr',
            field=models.IntegerField(max_length=300, primary_key=True, serialize=False),
        ),
    ]