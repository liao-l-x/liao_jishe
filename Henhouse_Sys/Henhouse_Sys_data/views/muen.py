from django.shortcuts import render,HttpResponse
from Henhouse_Sys_data import models
from Henhouse_Sys_data.views import fun

import json
def muen(request):
    if "log_user" in request.session.keys():
        Muen,user_info ,notice= fun.muen(request)
        return render(request,"muen/muen_sj.html",{"muen":Muen,"user_info":user_info,"notice":notice})
    else:
        return HttpResponse("请登入！！")
def muen_shuo(request):
    fowlery = models.company.objects.filter(name__contains =request.POST["muen_shuo"] ,hierarchy = 4)
    dict_company = []
    for f in fowlery:
        list_company = []
        list_company.append(f.name)
        list_company.append(f.lead.name)
        for i in models.company.hierarchy_list:
            if i[0] ==f.hierarchy:
                hierarchy_name = i[1]
                continue
        list_company.append(hierarchy_name)
        list_company.append(f.creat_Time)
        list_company.append(f.address)
        list_company.append(f.state)
        dict_company.append(list_company)
    return HttpResponse(json.dumps(dict_company))
def muen_user(request):
    if "log_user" in request.session.keys():
        Muen,user_info,notice = fun.muen(request)
        company =user_info.company
        list = fun.company_fun(company)
        user_dict = []
        for i in list:
            user_q = models.party_user.objects.filter(company=i).all()
            user_dict.extend(user_q)
    return render(request,"muen/mune_user.html",{"muen":Muen,"user_dict":user_dict,"user_info":user_info,"notice":notice})
def notice_info_app(request):
    if "log_user" in request.session.keys():
        Muen, user_info,notice = fun.muen(request)
        if request.method =="GET":
            user = models.party_user.objects.filter().all()
            return render(request,"muen/notice_info_app.html",
                          {"muen":Muen,"user_s":user,"user_info":user_info,"notice":notice})
        else:
            import time
            creat_Time = time.strftime("%Y-%m-%d %H:%M:%S")
            if request.POST['j_user'] != "notice":
                j_user_m = models.party_user.objects.filter(name=request.POST['j_user']).first()
                models.notice_info.objects.create(
                    title=request.POST["title"],
                    content=request.POST['content'],
                    j_user=j_user_m,
                    c_time = creat_Time,
                    c_user =user_info)
            else:
                models.notice_info.objects.create(
                    title=request.POST["title"],
                    content=request.POST['content'],
                    c_time = creat_Time,
                    c_user =user_info)
            return HttpResponse("成功")
def info(request):
    if "log_user" in request.session.keys():
        Muen, user_info,notice = fun.muen(request)
        if request.method == "GET":
            return render(request, "muen/info.html",
                          {"muen": Muen,
                           "user_info": user_info,
                           "notice": notice})
        else:
            #================================
            print(request.POST)
            return HttpResponse("成功")
def muen_xxx(requser):
    return HttpResponse("页面还没有！！！")