def usr_proxy(proxy_addr,url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read() .decode('utf-8')
    return data
def zhenzhe(data):
    import re
    gz = r'<ul class="clearfix sucai_list">(\w?|\w*)<div class="fenye">'
    data_re = re.compile(gz,re.S).findall(data)
    return data_re
def baocun(lujian,wenjian):
    print(wenjian)
    f = open(lujian,'w')
    # bytes(wenjian)
    for lsei in wenjian:
        f.write(lsei)
    f.close()
proxy_addr = "114.234.80.46:9000"
data = usr_proxy(proxy_addr,"http://ppt.xueshijr.com/s_2_0_0_0_0_1_.html")
e =3
lj = r"E:/xm/untitled/wj/"+str(e)+'.html'
# data_re = zhenzhe(data)
if(data):
    baocun(lj,data)
else:
    print('还是空的')