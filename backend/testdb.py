from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Academic, Collection, Education, Exhibition, Explanation, Museum, Museumnews, Museumrank, Usercomments, Userroles, Users
import json


def vuetest(request):
    if request.method == "POST":
        user=request.POST.get("username")
        pwd=request.POST.get("password")
        print()
        result = {"code": 20000,"data": {"token": "admin-token"}}
        print(HttpResponse(json.dumps(result), content_type="application/json"))
        #result=HttpResponse()
        #result.set_cookie(user,"v1")
        
        #return HttpResponse(json.dumps(result), content_type="application/json")
        return HttpResponse()

def infoo(request):
    if request.method == "GET":
        result = {"code": 20000, "data": {"roles": ["admin"], "introduction": "I am a super administrator",
                                       "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif", "name": "张昊"}}
        return HttpResponse(json.dumps(result), content_type="application/json")
# return HttpResponse(json.dumps(result))
def loginout(request):
    result={"code":20000,"data":"success"}
    return HttpResponse(json.dumps(result), content_type="application/json")

def Postman(request):
    result = 2
    result = request.method
    return HttpResponse(result)


def Test(request):
    Museum_list = Museum.objects.all()  # [:2]
    result = []
    i = 1
    for var in Museum_list:
        data = {}
        data['museumid'] = var.museumid,
        data['museumname'] = var.museumname,
        # data['introduction']=var.introduction,
        # data['opentime']=var.opentime,

        result.append(data)
        i += 1
    return HttpResponse(result)


def Add(request):
    museumid_add = 120
    museumname_add = '120testname'
    Museum.objects.create(museumid=museumid_add, museumname=museumname_add)
    result = []
    add_data = {}
    add_data['museumid'] = museumid_add,
    add_data['museumname'] = museumname_add,
    result.append(add_data)
    return HttpResponse(result)


def Delete(request):
    museumid_delete = 120
    Museum.objects.filter(museumid__contains=museumid_delete).delete()
    result = f"delete museumid:{museumid_delete}"
    return HttpResponse(result)


def Change(request):
    museumid_before = 120
    museumid_after = 200
    Museum.objects.filter(museumid__contains=museumid_before).update(
        museumid=museumid_after)
    result = f"change museumid from {museumid_before} to {museumid_after}"
    return HttpResponse(result)
