
from django.urls import path
#from backend.testdb import Postman,Test,Add,Delete,Change
import backend.testdb as api
import backend.test_comment_insert as api1
import backend.test_museum as api2
import backend.test_exhibition as api3
import backend.test_collection as api4
import backend.test_explanation as api5
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test',api.Test),
    path('add',api.Add),
    path('delete',api.Delete),
    path('change',api.Change),
    path('postman',api.Postman),
    path('loginin',api.vuetest),
    path('info',api.infoo),
    path('loginout',api.loginout),

    path('exhibition',api.TestEx),
    path('news',api.News),
    path('citymuseum',api.Citymuseum),

    path('commenttest',api1.comment_test),
    path('commenttestadmin',api1.comment_add),
    path('commentget',api1.comment_get),
    path('commentadd',api1.comment_add),
    path('commentdelete',api1.comment_delete),
    path('commentchange',api1.comment_change),

    path('museumtest',api2.museum_test),
    path('museumadd',api2.museum_add),
    path('museumdelete',api2.museum_delete),
    path('museumchange',api2.museum_change),

    path('exhibitiontest',api3.exhibithion_test),
    path('exhibitionadd',api3.exhibition_add),
    path('exhibitiondelete',api3.exhibition_delete),
    path('exhibitionchange',api3.exhibition_change),

    path('collectiontest',api4.collection_test),
    path('collectionadd',api4.collection_add),
    path('collectiondelete',api4.collection_delete),
    path('collectionchange',api4.collection_change),

    path('explanationtest',api5.explanation_test),
    path('explanationadd',api5.explanation_add),
    path('explanationdelete',api5.explanation_delete),
    path('explanationchange',api5.explanation_change),



]

