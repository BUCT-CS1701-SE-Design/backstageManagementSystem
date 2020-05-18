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

def explanation_test(request):
    Explanation_list = Explanation.objects.all()
    '''
    result = []
    i = 1
    for var in Explanation_list:
        data = {}
        #type
        data['explanationid'] = var.explanationid,
        data['explanationname'] = var.explanationname,
        data['explainerid'] = var.explainerid,
        data['explanationtime'] = var.explanationtime,
        #state
        data['total'] = len(Explanation_list),
        data['code'] = 200,
        result.append(data)
        i += 1
    data['total'] = len(Explanation_list),
    data['code'] = 200,
    result.append(data)
    return HttpResponse(json.dumps(result))
'''
    jsondata = serializers.serialize('json',Explanation_list)
    return HttpResponse(jsondata)

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
