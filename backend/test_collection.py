from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Academic, Collection, Education, Exhibition, Explanation, Museum, Museumnews, Museumrank, Usercomments, Userroles, Users
import json
from django.core import serializers

def vuetest(request):
    if request.method == "POST":
        result = {"code": 20000, "data": {"token": "admin-token"}}
        return HttpResponse(json.dumps(result), content_type="application/json")


def infoo(request):
    if request.method == "GET":
        result = {"code": 20000, "data": {"roles": ["admin"], "introduction": "I am a super administrator",
                                       "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif", "name": "张昊"}}
        return HttpResponse(json.dumps(result), content_type="application/json")
# return HttpResponse(json.dumps(result))


def Postman(request):
    result = 2
    result = request.method
    return HttpResponse(result)



def collection_test(request):
    Collection_list = Collection.objects.all()
    '''
    result = []
    i = 1
    for var in Collection_list:
        data = {}
        data['museumid'] = var.museumid,
        data['collectionID'] = var.collectionid,
        data['collectionName'] = var.collectionname,
        data['collectionIntroduntion'] = var.collectionintroduction,
        data['collectionimage'] = var.collectionimage,
        result.append(data)
        i += 1
    data['total'] = len(Collection_list),
    data['code'] = 200,
    result.append(data)
    return HttpResponse(result)
'''
    jsondata = serializers.serialize('json',Collection_list)
    return HttpResponse(jsondata)


def collection_add(request):
    museumid_add = 200
    collectionid_add = 000
    collectionname_add = 'xxx'
    collectionIntroduntion_add = 'xxx'
    collectionimage_add = '000'
    Collection.objects.create(museumid=museumid_add,collectionid=collectionid_add, collectionname=collectionname_add,collectionintroduction=collectionIntroduntion_add,collectionimage=collectionimage_add)

    result = []
    data = {}
    data['museumid'] = museumid_add,
    data['collectionID'] = collectionid_add,
    data['collectionName'] = collectionname_add,
    data['collectionIntroduntion'] = collectionIntroduntion_add,
    data['collectionimage'] = collectionimage_add,
    result.append(data)
    return HttpResponse(result)


def collection_delete(request):
    collectionid_delete = 200
    Collection.objects.filter(collectionid__contains=collectionid_delete).delete()
    result = f"delete museumid:{collectionid_delete}"
    return HttpResponse(json.dumps(result))


def collection_change(request):
    collectionid_before = 400
    collectionid_after = 400
    museumid_after = 200
    collectionname_after = 'xxx'
    collectionintroduction_after = 'xxx'
    collectionimage_after = 'xxx'

    Collection.objects.filter(collectionid__contains=collectionid_before).update(museumid=museumid_after,collectionid=collectionid_after,collectionname=collectionname_after,collectionintroduction= collectionintroduction_after,collectionimage=collectionimage_after)

    result = f"change collectionid from {collectionid_before} to {collectionid_after}"
    return HttpResponse(json.dumps(result))
