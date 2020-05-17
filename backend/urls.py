from django.urls import path
#from backend.testdb import Postman,Test,Add,Delete,Change
import backend.testdb as api

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test',api.Test),
    path('add',api.Add),
    path('delete',api.Delete),
    path('change',api.Change),
    path('postman',api.Postman),
    path('vuetest',api.vuetest),
    path('info',api.infoo),
    path('loginout',api.loginout)
]