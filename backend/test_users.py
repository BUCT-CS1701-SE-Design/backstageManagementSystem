from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from backend.models import Academic, Collection, Education, Exhibition, Explanation, Museum, Museumnews, Museumrank, Usercomments, Userroles, Users
import json
from django.core import serializers
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout

def users_test(request,id):
    testdata = int(id)
    Users_list = Users.objects.filter(userid =testdata)
    result = {}
    jsondata = serializers.serialize('json', Users_list)
    jsondatautf8 = json.loads(jsondata, encoding='utf-8')
    result = {
        "code": 200,
        "data": {
            "total": len(Users_list),
            "items": jsondatautf8}
    }

    return JsonResponse(result)



def users_add(request):
    usersid_add = 200
    username_add = '120testname'
    nickname_add = 'xxx'
    telephone_add = 'xx'
    idcard_add = 'xx'
    userrole_add = 'xx'
    usercreatedate_add = 'xx'

    Users.objects.create(userid=usersid_add, username=username_add,nickname = nickname_add,telephone= telephone_add,idcard= idcard_add,userrole = userrole_add,usercreatedate=usercreatedate_add)

    result = usersid_add
    return HttpResponse(result)


def users_delete(request):
    usersid_delete = 200
    Users.objects.filter(userid__contains=usersid_delete).delete()
    result = f"delete usersid:{usersid_delete}"

    return HttpResponse(json.dumps(result))

def users_change(request):
    userid_change= 12
    changedata= Users.object.get(userid = userid_change)
    changedata.username = 'xx'
    changedata.nickname = 'xx'

    changedata.save()
    return HttpResponse(result)