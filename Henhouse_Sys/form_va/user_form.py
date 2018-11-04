from  django import  forms
from django.forms import widgets
class user_log_From(forms.Form):
    name = forms.CharField(max_length=12,label='用户名')
    pwd = forms.CharField(max_length=20,label='密码',
                          widget=widgets.PasswordInput(render_value=True))
# class user_create_From(forms.Form):
