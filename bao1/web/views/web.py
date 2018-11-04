from django.shortcuts import render,HttpResponse
from dataManage import  models

# Create your views here.
def index(ret,*k,**kwargs):
    user_s = models.user1.objects.filter(id=ret.session['user'])
    zyfenlei_list = models.article.zyfenlei_s
    if kwargs:
        article_s = models.article.objects.filter(zyfenlei=kwargs['zyfenlei'])
        kwargs['zyfenlei'] = str(kwargs['zyfenlei'])
        return render(ret, 'zy/index.html',
                      {
                          'kwargs':kwargs,
                          'user_s':user_s[0],
                          'zyfenlei_list':zyfenlei_list,
                         'article_s': article_s,
                      })
    else:
        article_s = models.article.objects.all()
        return render(ret, 'zy/index.html', {
            'user_s': user_s[0],
            'zyfenlei_list': zyfenlei_list,
            'article_s': article_s,
        })