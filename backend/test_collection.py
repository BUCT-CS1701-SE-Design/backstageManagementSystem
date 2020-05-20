from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from backend.models import Academic, Collection, Education, Exhibition, Explanation, Museum, Museumnews, Museumrank, Usercomments, Userroles, Users
import json
from django.core import serializers
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout


def collection_test(request):
    testdata = 12
    Collection_list = Collection.objects.filter(museumid = testdata)
    result = {}
    jsondata = serializers.serialize('json', Collection_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(Collection_list),
            "items": jsondatautf8}
    }
    return JsonResponse(result)
def collection_All(request):
    Collection_list = Collection.objects.all()
    result = {}
    jsondata = serializers.serialize('json', Collection_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(Collection_list),
            "items": jsondatautf8}
    }
    return JsonResponse(result)

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
