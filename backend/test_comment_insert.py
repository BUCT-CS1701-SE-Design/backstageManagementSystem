from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Academic, Collection, Education, Exhibition, Explanation, Museum, Museumnews, Museumrank, Usercomments, Userroles, Users
import json

def comment_test(request):
    result = []
    data = {}
    if Usercomments.objects.filter(status=1).exists():
        data['userid'] = Users.objects.filter(userid=000).exists(),
        data['museumid'] = Museum.objects.filter(museumid=000).exists(),
        data['museumname'] = Museum.objects.filter(museumname='xxx').exists(),
        #data['commentdate'] = Usercomments.objects.filter(commentdate=xxx).exists()
        data['comment'] = Usercomments.objects.filter(comment='xxx').exists(),

    result.append(data)

    return HttpResponse(result)

def comment_test_admin(request):
    result = []
    data = {}
    data['userid'] = Users.objects.filter(userid=000).exists(),
    data['museumid'] = Museum.objects.filter(museumid=000).exists(),
    data['museumname'] = Museum.objects.filter(museumname='xxx').exists(),
    #data['commentdate'] = Usercomments.objects.filter(commentdate=xxx).exists()
    data['comment'] = Usercomments.objects.filter(comment='xxx').exists(),
    result.append(data)
    return HttpResponse(json.dumps(result))

def comment_add(request):
    userid_add = 400
    museumid_add = 400
    museumname_add = 'xxx'
    #commentdate_add = 000
    comment_add = 'xxx'
    Usercomments.objects.create(userid=userid_add, museum=museumid_add,museumname=museumid_add,comment=comment_add)
    result = []
    add_data = {}
    add_data['userid'] = userid_add
    add_data['museumid'] = museumid_add,
    add_data['museumname'] = museumname_add,
    #add_data['commentdate'] = commentdate_add,
    add_data['comment'] = comment_add,
    result.append(add_data)
    return HttpResponse(json.dumps(result))


def comment_delete(request):
    commentid_delete = 000
    if Usercomments.objects.filter(commentid=commentid_delete).exists():
        Usercomments.objects.filter(status = 1).update(status = 0)
    return HttpResponse(json.dumps(commentid_delete))


def comment_change(request):
    userid_before = 400
    museumid_before = 400
    museumname_before = 'xxx'
    # commentdate_before = 000
    comment_before = 'xxx'
    userid_after = 400
    museumid_after = 400
    museumname_after = 'xxx'
    # commentdate_after = 000
    comment_after = 'xxx'

    Usercomments.objects.filter(userid__contain=userid_before).update(userid=userid_after)
    Usercomments.objects.filter(museumid__contain=museumid_before).update(museumid=museumid_after)
    Usercomments.objects.filter(museumname__contain=museumname_before).update(museumname=museumname_after)
    Usercomments.objects.filter(comment__contain=comment_before).update(comment=comment_after)
    #Usercomments.objects.filter(commentdate__contain=commentdate_before).update(commentdate=commentdate_after)

    result = f"""change userid from {userid_before} to {userid_after},
change museumid from {museumid_before} to {museumid_after},
change museumname from {museumname_before} to {museumname_after},
change comment from {comment_before} to {comment_after},
"""#change commentdate from {commentdate_before} to {commentdate_after},

    return HttpResponse(json.dumps(result))


