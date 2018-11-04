from  django import  forms
from django.forms import widgets

class userFrom(forms.Form):
    name = forms.CharField(max_length=12,label='用户名')
    pwd = forms.CharField(max_length=20,label='密码')
    mail = forms.CharField(max_length=20,label='邮件')
    img = forms.ImageField(label='头像')