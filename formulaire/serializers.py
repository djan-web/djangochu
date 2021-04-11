from rest_framework import serializers
from .models import Patient

class Esp32Ser(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['codebr', 'Nom','Status','date_creation','date']