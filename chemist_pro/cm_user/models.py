from django.db import models
from db.base_model import BaseModel
from util.get_hashlib import get_hash
from util.get_hashlib import put_bcrypt
import time

class PassportManager(models.Manager):
    '''用户模型管理器类'''
    def add_one_passport(self,tel,password):
        '''添加用户：电话，密码'''
        # passport = self.create(tel = tel,password = put_bcrypt(password))
        passport = self.create(tel = tel,password = get_hash(password))
        return passport

class Passport(BaseModel):
    '''用户模型'''
    user =  str(int(time.time()*10000))[6:]
    username = models.CharField(max_length=20, default=user,verbose_name='用户名')
    password = models.CharField(max_length=60,verbose_name='密码')
    tel = models.CharField(max_length = 20,verbose_name = '电话号码')
    email = models.EmailField(verbose_name = '邮箱')
    is_shop = models.BooleanField(default=False,verbose_name='店铺状态')
    # 创建模型管理器类对象
    objects = PassportManager()

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        db_table = 'cm_user'

    def def__unicode__(self):
        return self.username

    def __str__(self):
        return self.username







