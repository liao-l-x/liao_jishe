from django.shortcuts import render,HttpResponse,redirect
from Henhouse_Sys_data import models
from form_va.user_form import user_log_From
from Henhouse_Sys_data.views import user_m

def create_user(request):
    """
    都需要验证session
    get:把页面，以及下属一层的公司的数据库对象
    post:前端需要提交 name pwd company phone sex
    """
    user_id = request.session['log_user']  # 数据类型有问题  18-11-1
    user_info = models.party_user.objects.filter(id=user_id).first()
    part_info = models.part.objects.filter(part=user_info.part).first()
    if (request.method =="GET"):
        if(user_info.part.part == "超级管理员" and user_info.company == None):#超管
            #所有公司
            branch_company = models.company.objects.filter().all()
        else:
            company_info = models.company.objects.filter(name=user_info.company).first()#所在公司，可以为空--超管
        #拿出下属一层公司
            branch_company = user_m.branch_company(company_info,[])
        return render(request, "user/create.html",{"branch_company":branch_company,"title":"创建"})
    else:
        create_user_info = request.POST
        company = models.company.objects.filter(name=create_user_info["company"]).first()
        part_info_c = models.part.objects.filter(id=part_info.id +1).first()
        print(type(company))
        import time
        creat_Time = time.strftime("%Y-%m-%d %H:%M:%S")
        models.party_user.objects.create(
            name = create_user_info["name"],
            pwd = create_user_info["pwd"],
            part = part_info_c,
            company=company,
            sex = create_user_info["sex"],
            phone = create_user_info["phone"],
            creat_Time = creat_Time)
        return HttpResponse("创建成功,用户名为"+create_user_info["name"]+"密码为"+create_user_info["pwd"])
def log_user(request):
    """
    post:前端要提交两个数据  maen  pwd
    """
    if (request.method == "GET"):
        user_form = user_log_From()
        return render(request, "user/log.html",{"user_form":user_form,"title":"登入"})
    elif(request.method=="POST"):
        user_log_info = user_log_From(request.POST)
        if user_log_info.is_valid():
            values = user_log_info.clean()#前端提交的数据=》字典
            user_info = models.party_user.objects.filter(**values).first()
            if(user_info):
                request.session["log_user"]  = user_info.id
                return redirect("/muen/muen.html")
        else:
            return render(request, "user/log.html",{"title":"登入"})#登入失败
def log_no_user(request):
    del request.session['log_user']
    return HttpResponse("退出登录成功")
