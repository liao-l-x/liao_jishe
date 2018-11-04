from django.shortcuts import render,HttpResponse,redirect
from dataManage import  models
from kit.xxfrom import userFrom
def loings(ret):
    content = ret.POST
    if not content:
        return render(ret, 'enter/loing.html')
    data = models.user1.objects.filter(name=content['user'],pwd=content['pwd'])
    if data:
        ret.session['user'] = data[0].id
        return redirect('/web/index')
    else:
        return render(ret, 'enter/loing.html')

def enroll(ret):
    if ret.method == 'GET':
        obj = userFrom()
        return  render(ret,'enter/enroll.html',{'obj':obj})
    else:
        obj = userFrom(ret.POST,ret.FILES)
        if obj.is_valid():
            xin_user = models.user1.objects.create(**obj.cleaned_data)
            ret.session['user'] = xin_user.id
            return redirect('/web/index')
        else:
            return render(ret, 'enter/enroll.html', {'obj': obj})
def user_eidt(ret):#图片待处理
    if ret.method == "GET":
        user_id = ret.session['user']
        user = models.user1.objects.filter(id = user_id).first()
        userfrom = userFrom({'name':user.name,'pwd':user.pwd,'mail':user.mail,'img':user.img})
        return render(ret,'enter/user_eidt.html',{'userfrom':userfrom,'img':user.img})
    else:
        print(111,ret.POST)
        if not ret.POST['img']:
            print('图片没有修改！')

        else:
            print(ret.POST["img"],"图片上传成功")


