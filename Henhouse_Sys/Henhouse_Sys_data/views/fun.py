def muen(request):
    """

    :param request: 请求信息
    :return: Muen  菜单树   user_info 用户信息
    """
    from Henhouse_Sys_data import models
    user_id = request.session['log_user']  # 数据类型有问题  18-11-1
    user_info = models.party_user.objects.filter(id=user_id).first()
    if user_info.company:
        Muen = models.muen.objects.filter(muen_a__gte=user_info.company.hierarchy).all()
    else:
        Muen = models.muen.objects.filter().all()
    s_x = models.notice_info.objects.filter(j_user=user_info,state=None).count()
    t_z = models.notice_info.objects.filter(j_user=None).count()
    notice = []
    notice.append(s_x)
    notice.append(t_z)
    return Muen,user_info,notice

def company_fun(company_):
    """
    参数：company_:公司的数据库对象
    return：一个list  里面是数据库对象
    """
    from Henhouse_Sys_data.models import company
    company_s = company.objects.filter(lead=company_.id).all()
    list = []
    for company_s_i in company_s:
        list.append(company_s_i)
        if company_s_i.hierarchy<4:
            d = company_fun(company_s_i)
            list.extend(d)
    return list


