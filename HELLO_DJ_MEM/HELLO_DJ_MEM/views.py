from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from HELLO_DJ_MEM.daomem import DaoMem




def mem_list(request):
    de = DaoMem()
    list = de.selectList()
    return render(request, 'mem_list.html', {'list': list})

def mem_detail(request):
    m_id = request.GET.get('m_id','')
    de = DaoMem()
    vo = de.selectOne(m_id)
    return render(request, 'mem_detail.html', {'vo': vo})

def mem_mod(request):
    m_id = request.GET.get('m_id','') #URL 주소값을 받아야 하므로 GET방식!
    de = DaoMem()
    vo = de.selectOne(m_id) #update 말고 selectOne으로 해야 수정화면으로 넘어감
    return render(request, 'mem_mod.html', {'vo': vo})

def mem_mod_act(request):
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    email = request.POST['email']

    de = DaoMem()
    cnt = de.update(m_id, m_name, tel, email) 

    return render(request, 'mem_mod_act.html', {'cnt': cnt})

def mem_add(request):
    return render(request, 'mem_add.html')

def mem_add_act(request):
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    email = request.POST['email']
    de = DaoMem()
    cnt = de.insert(m_id, m_name, tel, email) 

    return render(request, 'mem_add_act.html', {'cnt': cnt})

def mem_del_act(request):
    m_id = request.POST['m_id'] 
    de = DaoMem()
    cnt = de.delete(m_id)
    return render(request, 'mem_del_act.html', {'cnt': cnt})





