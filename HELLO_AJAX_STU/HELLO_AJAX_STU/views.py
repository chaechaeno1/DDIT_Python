from django.shortcuts import HttpResponse, redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseRedirect, JsonResponse
from django.urls import reverse

import json
from HELLO_AJAX_STU.daostudent import DaoStudent

def index(request):
    #return HttpResponse("Hello, Django")
    #return redirect('static/student.html')
    return HttpResponse("<script>location.href='static/student.html';</script>")

@csrf_exempt
def ajax_selectlist(request):
    #list를 불러올때는 request 받을 변수가 없으므로
    #dict = json.loads(request.body) 불필요
    
    #dao 선언
    de = DaoStudent()
    list = de.selectList()
    json = {
        'list': list
    }
    return JsonResponse(json)


@csrf_exempt
def ajax_select(request):
    #HTTP를 이용한 통신을 할 때 
    #POST Method를 이용해 Request를 받을 경우
    #dict = json.loads(request.body) 사용
    dict = json.loads(request.body)
    s_id = dict['s_id']

    de = DaoStudent()
    vo = de.selectOne(s_id)
    context = {
        'vo': vo,
    }
    return JsonResponse(context)

#insert는 파라미터 4개 모두 받고
#dao에다가 insert
#cnt로 받음

@csrf_exempt
def ajax_insert(request):
    #HTTP를 이용한 통신을 할 때 
    #POST Method를 이용해 Request를 받을 경우
    #dict = json.loads(request.body) 사용
    dict = json.loads(request.body)
    
    #파라미터 받는 것들
    #insert니까 4개 값 다 받아야함
        
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    grade = dict['grade']
    
    de = DaoStudent()
    cnt = de.insert(s_id, s_name, mobile, grade)
    
    context = None
    list = None
    
    if cnt == 1 : #추가 성공했을 경우
        list = de.selectList()
        context = {
            'cnt': cnt,
            'list': list,
        }
    else : #추가 실패했을 경우 
        context = {
            'cnt': cnt,
        }
        
    return JsonResponse(context)

#추가했을 때 방법 2가지
#cnt 1값이면 emp.html 부르기
#list : list 로 해주기


@csrf_exempt
def ajax_update(request):
    #HTTP를 이용한 통신을 할 때 
    #POST Method를 이용해 Request를 받을 경우
    #dict = json.loads(request.body) 사용
    dict = json.loads(request.body)
    
    #4개 받아와야함    
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    grade = dict['grade']
    
    de = DaoStudent()
    cnt = de.update(s_id, s_name, mobile, grade)
    
    context = None
    list = None
    
    if cnt == 1 : #수정 성공했을 경우
        list = de.selectList()
        context = {
            'cnt': cnt,
            'list': list,
        }
    else : #추가 실패했을 경우 
        context = {
            'cnt': cnt,
        }
        
    return JsonResponse(context)


@csrf_exempt
def ajax_delete(request):
    #HTTP를 이용한 통신을 할 때 
    #POST Method를 이용해 Request를 받을 경우
    #dict = json.loads(request.body) 사용
    dict = json.loads(request.body)
      
    s_id = dict['s_id']
    
    de = DaoStudent()
    cnt = de.delete(s_id)
    
    context = None
    list = None
    
    if cnt == 1 : #수정 성공했을 경우
        list = de.selectList()
        context = {
            'cnt': cnt,
            'list': list,
        }
    else : #추가 실패했을 경우 
        context = {
            'cnt': cnt,
        }
        
    return JsonResponse(context)

    



