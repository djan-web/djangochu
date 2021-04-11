from django.forms import ModelForm
from .models import Patient
import datetime

class PatientForm(ModelForm):

	class Meta:
		model = Patient
		fields = '__all__'
