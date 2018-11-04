from django.db import models

# Create your models here.
#用户
class user(models.Model):
    name = models.CharField(max_length=12,verbose_name='用户名')
    pwd = models.CharField(max_length=20,verbose_name='密码')
    mail = models.CharField(max_length=20,verbose_name='邮箱')
    img = models.ImageField(upload_to = "static/user_img/",verbose_name='头像' )
    def __srt__(self):
        return self.name
    class Meta:
        verbose_name= "用户表"
        verbose_name_plural ="用户表"
#博客
class boke(models.Model):
    suffixURL = models.CharField(max_length=10,verbose_name='后缀名')
    theme = models.CharField(max_length=20,verbose_name="个人主题")
    title = models.CharField(max_length=20,verbose_name='标题')
    present = models.CharField(max_length=50,verbose_name='基本介绍')
    user_id = models.OneToOneField(user,on_delete=None,verbose_name='博客主人')
    def __srt__(self):
        return self.suffixURL
    class Meta:
        verbose_name = "博客表"
        verbose_name_plural= "博客表"
#粉丝
class fufen(models.Model):
    star_Id = models.ForeignKey(user,verbose_name='明星',on_delete=None,parent_link=True,related_name='user_star',)
    fans_id = models.ForeignKey(user,verbose_name='粉丝',on_delete=None,parent_link=True,related_name='user_fans',)
    class Meta:
        verbose_name = "粉丝表"
        verbose_name_plural ="粉丝表"
#报障单
class ensure(models.Model):
    title = models.CharField(max_length=20,verbose_name='标题')
    content = models.CharField(max_length=255,verbose_name='内容')
    T_user = models.OneToOneField(user,verbose_name='提问人',on_delete=None,parent_link=True, related_name='T_user')
    D_user = models.OneToOneField(user,verbose_name='回答人',on_delete=None,parent_link=True,null=True,related_name='D_user')
    state_s = {
        (0,'未处理'),
        (1, '处理中'),
        (2, '已处理')
    }
    state = models.IntegerField(choices=state_s,default=0,verbose_name='状态')
    C_time = models.DateTimeField(verbose_name='创建时间')
    T_time = models.DateTimeField(verbose_name='处理时间')
    class Meta:
        verbose_name = "报障单"
        verbose_name_plural ="报障单"
#分类
# class clify(models.Model):
#     name = models.CharField(max_length=20,verbose_name="分类名")
#     boke_id = models.ForeignKey(boke,verbose_name='所属博客',on_delete=None,parent_link=True)
#     class Meta:
#         verbose_name = "分类表"
#         verbose_name_plural ="分类表"
#标签
class label(models.Model):
    label = models.CharField(max_length=20,verbose_name="标签名")
    boke_id = models.ForeignKey(boke,verbose_name='所属博客',on_delete=None,parent_link=True,)
    class Meta:
        verbose_name = "标签表"
        verbose_name_plural ="标签表"
#文章大概
class article(models.Model):
    title = models.CharField(max_length=50)
    C_time = models.DateTimeField(verbose_name="创建时间")
    # c_id = models.ForeignKey(clify,on_delete=None,parent_link=True,verbose_name='分类')
    label_id = models.ManyToManyField(label,verbose_name='文章标签')
    class Meta:
        verbose_name = "文章信息"
        verbose_name_plural = "文章信息"
#文章内容
class article_nr(models.Model):
    content = models.CharField(max_length=255,verbose_name='内容')
    article_xx_id = models.OneToOneField(article,on_delete=None,verbose_name='文章信息')
    class Meta:
        verbose_name = "文章内容"
        verbose_name_plural = "文章内容"
#文章赞踩
class article_zan(models.Model):
    article_id = models.ForeignKey(article,on_delete=None,parent_link=True,verbose_name='文章')
    user_id = models.ForeignKey(user,on_delete=None,parent_link=True,verbose_name='用户')
    azn = models.BooleanField(verbose_name='赞')
    class Meta:
        unique_together = ('article_id', 'user_id',)#联合唯一
        verbose_name = "文章赞踩"
        verbose_name_plural = "文章赞踩"

class comment(models.Model):
    content = models.CharField(max_length=255,verbose_name='评论')
    article_id = models.ForeignKey(article,on_delete=None, parent_link=True, verbose_name='文章')
    user_id = models.ForeignKey(user,on_delete=None, parent_link=True, verbose_name='用户')
    comment_id = models.OneToOneField('self',on_delete=None, parent_link=True, verbose_name='用户')
    class Meta:
        verbose_name = "文章评论"
        verbose_name_plural = "文章评论"