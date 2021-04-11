# Generated by Django 3.1.5 on 2021-01-31 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codebr', models.CharField(max_length=300)),
                ('services', models.CharField(max_length=300)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]