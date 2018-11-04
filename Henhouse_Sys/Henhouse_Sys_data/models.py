from django.db import models

# Create your models here.
class part(models.Model):
    part = models.CharField(max_length=32,verbose_name="角色名称")
    part_a = models.CharField(max_length=32,verbose_name="角色权限")
    class Meta:
        verbose_name = "角色表"
    def __str__(self):
        return self.part
class party_user(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    pwd = models.CharField(max_length=32,verbose_name="密码")
    part = models.ForeignKey(to="part",on_delete=None,verbose_name="关联角色",parent_link=True)
    company = models.ForeignKey(to="company",on_delete=None,verbose_name="关联公司",null=True,blank=True,parent_link=True)
    sex_int = {
        ( '1','男'),
        ('2','女')
    }
    sex = models.CharField(max_length=2,choices =sex_int )
    phone = models.CharField(max_length=16,verbose_name="电话")
    state = models.TextField(verbose_name="状态",null=True,blank=True)
    creat_Time = models.CharField(max_length=32,verbose_name="创建时间")
    class Meta:
        verbose_name = "用户表"
    def __str__(self):
        return self.name
class company(models.Model):
    name = models.CharField(max_length=32,verbose_name="公司名字")
    lead = models.ForeignKey(to="company",on_delete=None,null=True,blank=True,verbose_name="被其领导")
    hierarchy_list={
        (1,"畜牧中心"),
        (2,"畜牧公司"),
        (3,"养殖场"),
        (4,"畜舍")
    }
    hierarchy = models.IntegerField(choices=hierarchy_list,verbose_name="层级")
    creat_Time = models.CharField(max_length=32,verbose_name="创建时间")
    address = models.TextField(verbose_name="地址")
    state = models.TextField(verbose_name="状态",null=True,blank=True)
    class Meta:
        verbose_name = "公司表"
    def __str__(self):
        return self.name
class barn_data(models.Model):
    company = models.ForeignKey(to="company",on_delete=None,verbose_name="畜舍")
    data = models.TextField(verbose_name="所有信息都暂时放在这")
    creat_Time = models.CharField(max_length=32,verbose_name="创建时间")
    class Meta:
        verbose_name = "畜舍信息"
    def __str__(self):
        return self.company
class muen(models.Model):
    name = models.CharField(max_length=32,verbose_name="菜单名称")
    hierarchy_list = {
        (1, "畜牧中心"),
        (2, "畜牧公司"),
        (3, "养殖场"),
        (4, "畜舍")
    }
    muen_a = models.IntegerField(choices=hierarchy_list,verbose_name="要求不低于这个权限")
    muen_hierarchy = models.ForeignKey(to="muen",on_delete=None,null=True,blank=True,verbose_name="它在那个菜单下")
    muen_class_name = models.CharField(max_length=32 ,null=True,blank=True,verbose_name="前端class的值")
    muen_url = models.CharField(max_length=32,null=True,blank=True,verbose_name="菜单url")
    class Meta:
        verbose_name = "菜单表"
    def __str__(self):
        return self.name

class notice_info(models.Model):
    title = models.CharField(max_length=32,verbose_name="标题")
    c_user =  models.ForeignKey(to="party_user",on_delete=None,verbose_name="发布人",parent_link=True,related_name="c_user")
    j_user = models.ForeignKey(to="party_user",on_delete=None,verbose_name="接受人",parent_link=True,null=True,blank=True,related_name="j_user")
    c_time =  models.CharField(max_length=32,verbose_name="创建时间")
    state = models.ForeignKey(to="party_user",verbose_name="状态", null=True, blank=True ,default='',on_delete=None)
    content = models.TextField(verbose_name="内容")

    class Meta:
        verbose_name = "通知信息表"
    def __str__(self):
        return self.title