
from django.urls import path
#from backend.testdb import Postman,Test,Add,Delete,Change
import backend.testdb as api
import backend.test_comment_insert as comment
import backend.test_museum as api2
import backend.test_exhibition as exhibition
import backend.test_collection as api4
import backend.test_explanation as api5
import backend.test_users as user

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

    path('collectionrank',api.Collectionrank),
    path('Newsrank',api.Newsrank),
    path('Exhibitionrank',api.Exhibitionrank),
    path('news',api.News),
    path('citymuseum',api.Citymuseum),
    path('exhibitionex',api.TestEx),
    path('news',api.News),
    path('citymuseum',api.Citymuseum),

    path('commenttest',comment.comment_test),
    path('commenttestadmin',comment.comment_add),
    path('comment_All',comment.comment_All),
    path('commentget',comment.comment_get),
    path('commentadd',comment.comment_add),
    path('commentdelete',comment.comment_delete),
    path('commentchange',comment.comment_change),

    path('museumtest/<int:id>/',api2.museum_test),
    path('museumadd',api2.museum_add),
    path('museumdelete',api2.museum_delete),
    path('museumchange',api2.museum_change),

    # path(r'^museumtesttest/$',api2.museum_testtest),

    path('exhibitiontest/<int:id>/',exhibition.exhibithion_test),
    path('exhibitionadd',exhibition.exhibition_add),
    path('exhibitionAll',exhibition.Exhibition_All),
    path('exhibajax',exhibition.Exhibition_pagin),
    path('exhibitiondelete',exhibition.exhibition_delete),
    path('exhibitionchange',exhibition.exhibition_change),
    path('exhibitionInfo/<int:pk>/',exhibition.exhibithionInfo),
    

    path('collectiontest/<int:id>/',api4.collection_test),
    path('collection_All',api4.collection_All),
    path('collectionadd',api4.collection_add),
    path('collectiondelete',api4.collection_delete),
    path('collectionchange',api4.collection_change),
    path('collectionInfo/<int:pk>/',api4.collection_Info),

    path('explanationtest',api5.explanation_test),
    path('explanationadd',api5.explanation_add),
    path('explanationdelete',api5.explanation_delete),
    path('explanationchange',api5.explanation_change),

    path('userstest',user.users_test),
    path('usersadd',user.users_add),
    path('usersdelete',user.users_delete),
    path('userschange',user.users_change),

]

