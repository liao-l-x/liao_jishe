from web.views import web,loing,grzy,manageuser
from django.urls import path,re_path



urlpatterns = [
    path('index/',web.index ),
    re_path('^index/(?P<zyfenlei>\d+).html$', web.index),
    path('loing',loing.loings),
    path('enroll',loing.enroll),
    path('grzy/',grzy.grzy),
    path('grzy/sqbk',grzy.sqbk),
    re_path('^grzy/(?P<suffixURL>\w+).html$',grzy.grzy),
    re_path('^(?P<suffixURL>\w+)/grzy/(?P<label>\d+)$', grzy.grfl),
    re_path('^(?P<suffixURL>\w+)/grzy/(?P<grfl>\w+).html$', grzy.grfl),

    path('user_eidt',loing.user_eidt),

    path('manage',manageuser.manage),
    re_path('manage-(?P<bq>\w+)-(?P<fl>\w+)', manageuser.manage),
    re_path('1edit/(?P<nid>\w+).html',manageuser.edit),
    path('1edit.html', manageuser.edit),

    re_path('^(?P<suffixURL>\w+)/(?P<wzid>\d+).html$', grzy.bkwz),

]