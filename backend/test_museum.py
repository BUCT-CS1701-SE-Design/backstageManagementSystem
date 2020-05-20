from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from backend.models import Academic, Collection, Education, Exhibition, Explanation, Museum, Museumnews, Museumrank, Usercomments, Userroles, Users
import json
from django.core import serializers
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout

def museum_test(request,id):
    testdata = int(id)
    Museum_list = Museum.objects.filter(museumid = testdata)
    result = {}
    jsondata = serializers.serialize('json', Museum_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(Museum_list),
            "items": jsondatautf8}
    }

    return JsonResponse(result)

def museum_add(request):
    museumid_add = 200
    museumname_add = '120testname'
    introduction_add = 'xxx'
    opentime_add = 'xxx'
    location_add = 'xxx'
    telephone_add = '000'
    link_add = 'xxx'
    Museum.objects.create(museumid=museumid_add, museumname=museumname_add,introduction=introduction_add,opentime=opentime_add,location=location_add,telephone=telephone_add,link=link_add)

    result = []
    data = {}
    data['museumid'] = museumid_add,
    data['museumname'] = museumname_add,
    data['introduction'] = introduction_add,
    data['opentime'] = opentime_add,
    data['location'] = location_add,
    data['telephone'] = telephone_add,
    data['link'] = link_add,

    result.append(data)
    return HttpResponse(result)


def museum_delete(request):
    museumid_delete = 200
    Museum.objects.filter(museumid__contains=museumid_delete).delete()
    result = f"delete museumid:{museumid_delete}"
    return HttpResponse(json.dumps(result))

def museum_change(request):
    museumid_before = 120

    museumid_after = 200
    introduction_after = 'xxx'
    opentime_after = 'xxx'
    location_after = 'xxx'
    telephone_after = '000'
    link_after = 'xxx'
    Museum.objects.filter(museumid__contains=museumid_before).update(
        museumid=museumid_after,introduction=introduction_after,opentime=opentime_after,location=location_after,telephone=telephone_after,link=link_after)

    result = f"change museumid from {museumid_before} to {museumid_after}"
    return HttpResponse(result)