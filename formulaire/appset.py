from rest_framework.viewsets import ModelViewSet
from .models import Patient
from .serializers import Esp32Ser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets


@api_view(['GET'])
##apiUrl
def PatListApi(request):
    all_pat = Patient.objects.all()
    data = Esp32Ser(all_pat, many=True).data
    return Response({'data':data})


class Esp32viewSet(viewsets.ModelViewSet):
    model = Patient
    queryset = Patient.objects.all()
    serializer_class = Esp32Ser


class Esp32views(generics.RetrieveUpdateAPIView):
    #model = Patient
    queryset = Patient.objects.all()
    serializer_class = Esp32Ser
    lookup_field = 'codebr'

