from django.urls import path
from . import views, appset

urlpatterns = [
    path('', views.index,name='acceuil'),
    path('tab/', views.pat,name='patient analyse'),
    path('db/', views.Dbord,name='tableau de bord'),

    ##api
    path('api/list', appset.PatListApi,name='ApiPatient'),

    ##generic
    path('api/', appset.Esp32viewSet.as_view({'get': 'list'}),name='ApiPatient'),
    path('api/<int:codebr>', appset.Esp32views.as_view(), name='ApiPatient'),

]