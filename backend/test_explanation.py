from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from backend.models import Academic, Collection, Education, Exhibition, Explanation, Museum, Museumnews, Museumrank, Usercomments, Userroles, Users
import json
from django.core import serializers
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout


def explanation_test(request):
    test_explanationid = 12
    Explanation_list = Explanation.objects.filter(explanationid = test_explanationid)
    result = {}
    jsondata = serializers.serialize('json', Explanation_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(Explanation_list),
            "items": jsondatautf8}
    }
    return JsonResponse(result)

def explanation_add(request):
    explanationid_add = 200
    explanationname_add = 'xxx'
    explainerid_add = 200
    explanationtime_add = 'xxx'
    Explanation.objects.create(explainerid= explainerid_add,explanationid=explanationid_add,explanationname=explanationname_add,explanationtime=explanationtime_add)

    result= explanationid_add
    return HttpResponse(json.dumps(result))


def explanation_delete(request):
    explanationid_delete = 0
    Explanation.objects.filter(explanation__contains=explanation_delete()).delete()
    result = f"delete explanationid:{explanation_delete()}"
    return HttpResponse(json.dumps(result))


def explanation_change(request):
    explanationid_before = 0

    explanationid_after = 200
    explanationname_after = 'xxx'
    explainerid_after = 200
    explanationtime_after = 'xxx'
    Explanation.objects.filter(explanationid__contains= explanationid_before).update(explanationid=explanationid_after)

    result = f"change explanationid from {explanationid_before} to {explanationid_after}"
    return HttpResponse(result)
