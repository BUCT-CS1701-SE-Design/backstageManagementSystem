from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from backend.models import Academic, Collection, Education, Exhibition, Explanation, Museum, Museumnews, Museumrank, Usercomments, Userroles, Users
import json
from django.core import serializers
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout

def exhibithion_test(request,id):
    testdata = int(id)
    Exhibition_list = Exhibition.objects.filter(museumid = testdata)
    result = {}
    jsondata = serializers.serialize('json',Exhibition_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(Exhibition_list),
            "items": jsondatautf8}
    }
    return JsonResponse(result)

def exhibithionInfo(request,pk):
    testdata = int(pk)
    Exhibition_list = Exhibition.objects.filter(pk = testdata)
    result = {}
    jsondata = serializers.serialize('json',Exhibition_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(Exhibition_list),
            "items": jsondatautf8}
    }
    return JsonResponse(result)

def Exhibition_All(request):
    Exhibition_list = Exhibition.objects.all()
    result = {}
    jsondata = serializers.serialize('json',Exhibition_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(Exhibition_list),
            "items": jsondatautf8}
    }
    return JsonResponse(result)

def Exhibition_pagin(request):
    Exhibition_list = Exhibition.objects.all()[:1]
    result = {}
    jsondata = serializers.serialize('json',Exhibition_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(Exhibition_list),
            "items": jsondatautf8}
    }
    return JsonResponse(result)

def exhibition_add(request):
    museumid_add = 200
    exhibitiontheme_add= 'xxx'
    exhibitionid_add = 0
    exhibitionpicture_add = 'xx'
    Exhibition.objects.create(museumid=museumid_add,exhibitionid=exhibitionid_add,exhibitiontheme=exhibitiontheme_add,exhibition_picture=exhibitionpicture_add)

    result = []
    data = {}
    data['museumid'] = museumid_add,
    data['exhibitionTheme'] = exhibitiontheme_add,
    data['exhibitionID'] = exhibitionid_add,
    data['exhibition_picture'] = exhibitionpicture_add,

    result.append(data)
    return HttpResponse(result)


def exhibition_delete(request):
    exhibitionid_delete = 0
    Exhibition.objects.filter(exhibitionid__contains=exhibitionid_delete).delete()
    result = f"delete exhibitionid:{exhibitionid_delete}"
    return HttpResponse(json.dumps(result))


def exhibition_change(request):
    exhibitionid_before = 0

    exhibitionid_after = 0
    museumid_after = 200
    exhibitiontheme_after = 'xxx'
    #exhibition_picture_after
    Exhibition.objects.filter(exhibitionid__contains=exhibitionid_before).update(museumid=museumid_after,exhibitionid=exhibitionid_after,exhibitiontheme=exhibitiontheme_after)

    result = f"change exhibitionid from {exhibitionid_before} to {exhibitiontheme_after}"
    return HttpResponse(result)
