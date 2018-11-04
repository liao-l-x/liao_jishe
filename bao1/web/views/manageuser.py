from django.shortcuts import render,HttpResponse,redirect
from dataManage import  models

def manage(ret,**kwargs):
    """

    :param ret:
    :param kwargs:  "fl': ,"bq":
    :return:"bk": bk,  # 博客
            'wz': wz,  # 文章
            'fl': fenlei,  # 用户个人分类
            'bq': labels, # 用户标签
            'sx':kwargs,
    """

    r = ret.session['user']  # id  user1
    bk = models.boke.objects.filter(user_id=r).first()
    if not bk:
        user = models.user1.objects.filter(id=r).first()
        return render(ret, 'grzy/qsbk.html', {
            'user': user
        })
    wz = models.article.objects.filter(author=bk.user_id)
    fenlei = models.clify.objects.filter(boke_id=bk.id)
    labels = models.label.objects.filter(boke_id=bk.id)
    if 'fl' in kwargs.keys():
        if kwargs['fl'] != 'x':
            wz = wz.filter(c_id=int(kwargs['fl']))
    else:
        kwargs['fl'] = '0'
    if 'bq' in kwargs.keys():
        if  kwargs['bq'] != 'x':
            wz = wz.filter(label_id=int(kwargs['bq']))
    else:
        kwargs['bq'] = '0'
    return render(ret, 'gegl/glzy.html', {
        "bk": bk,  # 博客
        'wz': wz,  # 文章
        'fl': fenlei,  # 用户个人分类
        'bq': labels, # 用户标签
        'sx':kwargs,
    })
def edit(ret,**kwargs):
    if ret.method == 'GET':
        wz = models.article.objects.filter(id=kwargs['nid']).first()
        return render(ret,'gegl/gr-edit.html',{
            'wz':wz,
        })
    else:
        wz_xg = models.article.objects.filter(id=int(ret.POST['nid'][0])).update(title=ret.POST['title'])
        # print(type(wz_xg))
        models.article_nr.objects.filter(id=wz_xg).update(content=ret.POST['comtent'])
        return HttpResponse('修改成功！<a href="/web/manage">还回</a>')
