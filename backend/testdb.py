
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from backend.models import Academic, Collection, Education, Exhibition, Explanation, Museum, Museumnews, Museumrank, \
    Usercomments, Userroles, Users
import json
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.db.models import Count



# csrf认证
def get_csrf(request):
    # 生成 csrf 数据，发送给前端
    csrf_token = get_token(request)
    return JsonResponse({'token': csrf_token, 'code': 200})


def vuetest(request):
    if request.method == "POST":
        data = eval(request.body.decode()).get('username')
        username = json.loads(request.body).get('username')
        datap = eval(request.body.decode()).get('password')
        password = json.loads(request.body).get('password')
        user = authenticate(username=username, password=password)
        if user:
            result = {"data": {"token": "admin-token"}}
            result["code"] = 200
            # result=HttpResponse()
            # result.set_cookie(user,"v1")
            login(request, user)
            return HttpResponse(json.dumps(result), content_type="application/json")
        else:
            return HttpResponse("false")


def infoo(request):
    if request.method == "GET":
        result = {"data": {"roles": ["admin"], "introduction": "I am a super administrator",
                           "name": "admin"}}
        result["data"]["avatar"] = "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
        result["code"] = 200
        # print(result["data"]["avatar"])
        return HttpResponse(json.dumps(result), content_type="application/json")


# return HttpResponse(json.dumps(result))
def loginout(request):
    logout(request)
    result = {"code": 200, "data": "success"}
    return HttpResponse(json.dumps(result), content_type="application/json")


def Postman(request):
    result = 2
    result = request.method
    return HttpResponse(result)


def Test(request):
    Museum_list = Museum.objects.all()  # [:2]
    # result["code"] = 200
    result = {}
    i = 1
    jsondata = serializers.serialize('json', Museum_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    # data = {
    #     "code"=200,
    #     "data"=jsondata
    #     }
    result = {
        "code": 200,
        "data": {
            "total": len(Museum_list),
            "items": jsondatautf8}
    }
    # for var in Museum_list:
    #     data['museumid'] = var.museumid,
    #     data['museumname'] = var.museumname,
    # data['introduction']=var.introduction,
    # data['opentime']=var.opentime,

    # result.append(data)
    # i += 1
    return JsonResponse(result)


def TestEx(request):
    Exhibition_list = Exhibition.objects.all()
    jsondata = serializers.serialize('json',Exhibition_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')

    result = {
        "code": 200,
        "data": {
            "total": len(Exhibition_list),
            "items": jsondatautf8}
    }
    return  JsonResponse(result)

def News(request):
    News_list = Museumnews.objects.all()
    jsondata = serializers.serialize('json',News_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(News_list),
            "items": jsondatautf8}
    }
    return  JsonResponse(result)

def Citymuseum(request):
    city=request.GET.get('city')
    Museum_list=Museum.objects.filter(location__icontains=city)
    result =[]
    i=1
    for var in Museum_list:
        data={}
        data['museumname']=var.museumname
        data['museumid']=var.museumid
        data['location']=var.location
        
        result.append(data)
        i+=1
    fin=[]
    fin.append(result)
    jsondata = serializers.serialize('json',Museum_list)
    return HttpResponse(json.dumps(result))

def Collectionrank(request):
    rank_list=Museum.objects.order_by('collection_number')
    result=[]
    i=1
    for var in rank_list:
        if i<6:
            data={}
            data['rank']=i
            data['museumid']=var.museumid
            data['museumname']=var.museumname
            data['colllectionnum']=var.collection_number
            result.append(data)
        i+=1
        
    fin=[]
    fin.append(result)
    jsondata = serializers.serialize('json',rank_list)
    return HttpResponse(json.dumps(result))
    
def Newsrank(request):
    rank_list=Museum.objects.annotate(num=Count('museumnews__newsid')).order_by('-num')
    result=[]
    i=1
    for var in rank_list:
        if i<6:
            data={}
            data['rank']=i
            data['museumid']=var.museumid
            data['num']=var.num
            data['name']=var.museumname
            result.append(data)
        i+=1
       
    fin=[]
    fin.append(result)
    jsondata = serializers.serialize('json',rank_list)
    return HttpResponse(json.dumps(result))

def Exhibitionrank(request):
    rank_list=Museum.objects.annotate(num=Count('exhibition__exhibitionid')).order_by('-num')
    result=[]
    i=1
    for var in rank_list:
        if i<6:
            data={}
            data['rank']=i
            data['museumid']=var.museumid
            data['num']=var.num
            data['name']=var.museumname
            result.append(data)
        i+=1
        
    fin=[]
    fin.append(result)
    jsondata = serializers.serialize('json',rank_list)
    return HttpResponse(json.dumps(result))



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



