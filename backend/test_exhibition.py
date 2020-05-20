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

def exhibithion_test(request,id):
    testdata = 12
    Exhibition_list = Exhibition.objects.filter(museumid = testdata)
    '''
    result = []
    i = 1
    for var in Exhibition_list:
        data = {}
        data['museumid'] = var.museumid,
        data['exhibitionTheme'] = var.exhibitiontheme,
        data['exhibitionID'] = var.exhibitionid,
        data['exhibition_picture'] = var.exhibition_picture,
        result.append(data)
        i += 1
    data['total'] = len(Exhibition_list),
    data['code'] = 200,
    result.append(data)
    return HttpResponse(result)
'''
    jsondata = serializers.serialize('json',Exhibition_list)
    return HttpResponse(jsondata)

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
