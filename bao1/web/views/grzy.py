from django.shortcuts import render,HttpResponse,redirect
from dataManage import  models

def grzy(ret,**kwargs):
    """
    如果所有博客的url链接，还有用户进入自己的博客
    :param kwargs: kwargs['suffixURL']  = 博客后缀
    :return: "bk":bk,#博客
                'wz':wz,#文章
                'fl':fenlei,#用户个人分类
    """
    if kwargs:
        bk = models.boke.objects.filter(suffixURL = kwargs['suffixURL']).first()
    else:
        r = ret.session['user']#id  user1
        bk = models.boke.objects.filter(user_id = r).first()
        if not bk:
            user = models.user1.objects.filter(id=r).first()
            return render(ret,'grzy/qsbk.html',{
                'user':user
            })
    wz = models.article.objects.filter(author=bk.user_id)
    fenlei = models.clify.objects.filter(boke_id =bk.id )
    labels = models.label.objects.filter(boke_id=bk.id)
    return render(ret,'grzy/grzy.html',{
        "bk":bk,#博客
        'wz':wz,#文章
        'fl':fenlei,#用户个人分类
        'bq': labels  # 用户标签
    })

def grfl(ret,**kwargs):
    """
            分类筛选，按分类
    :param ret:
    :param kwargs: kwargs['suffixURL'] = 博客后缀   kwargs['grfl'] = 个人分类
    :return: "bk": bk,  # 博客
                'wz': wz,  # 文章
                'fl': fenlei,  # 用户个人分类
    """
    # print(kwargs['suffixURL'])#返回后缀
    # print(type(kwargs['grfl']))#个人分类
    # print(type(ret.session['user']))#用户id
    bk = models.boke.objects.filter(suffixURL=kwargs['suffixURL']).first()#博客
    if 'label' in kwargs.keys():
        labelq = models.label.objects.filter(id=kwargs['label']).first()
        wz = models.article.objects.filter(label_id=labelq.id)
    else:
        wz = models.article.objects.filter(c_id__name=kwargs['grfl'])
    fenlei = models.clify.objects.filter(boke_id=bk.id)
    labels = models.label.objects.filter(boke_id=bk.id)
    return render(ret, 'grzy/grfl.html', {
        "bk": bk,  # 博客
        'wz': wz,  # 文章
        'fl': fenlei,  # 用户个人分类
        'bq':labels#用户标签
    })

def bkwz(ret,**kwargs):
    # print(kwargs['suffixURL'])#博客后缀
    # print(kwargs['wzid'])#文章信息id
    wzxx = models.article.objects.filter(id = kwargs['wzid']).first()
    return render(ret,'grzy/wzym.html',
                  {
                      'wzxx':wzxx,
                  })

def sqbk(ret,**kwargs):
    #申请博客
    r = ret.session['user']  # id  user1
    user = models.user1.objects.filter(id=r).first()
    str_div =''
    for k,v in ret.POST.items():
        if not k =='user_id':
            str_div = str_div+k+'='+'"'+v+'"'+','
    t = 'models.boke.objects.create('+str_div+ 'user_id'+'='+'user'+')'
    eval(t)
    return redirect('/web/grzy/'+ret.POST['suffixURL']+'.html')