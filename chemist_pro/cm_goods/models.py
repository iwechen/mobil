from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField


class ShopManager(models.Manager):
    '''店铺模型管理器类'''
    pass

class Shop(BaseModel):
    '''店铺模型类'''
    name = models.CharField(max_length=20,verbose_name ='店铺名称')
    addr = models.CharField(max_length=128,verbose_name = '店铺地址')
    detail = HTMLField(verbose_name='店铺详情')
    objects = ShopManager()
    class Meta:
        db_table = 'cm_shop'
        verbose_name = '店铺s'
        verbose_name_plural = verbose_name
    def def__unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class TypeManager(models.Manager):
    '''种类模型管理器类'''
    pass

class Type(BaseModel):
    '''商品种类模型类'''
    name = models.CharField(max_length=20,verbose_name ='种类名称')
    image = models.ImageField(upload_to='goods',verbose_name='种类图标')
    objects = TypeManager()
    class Meta:
        db_table = 'cm_type'
        verbose_name = '种类'
        verbose_name_plural = verbose_name
    def def__unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class GoodsManager(models.Manager):
    '''种类模型管理器类'''
    def get_goods_by_id(self,goods_id):
        '''根据id查询商品信息'''
        try:
            goods = self.get(id=goods_id)
        except self.model.DoesNotExist:
            goods = None
        return goods

class Goods(BaseModel):
    '''商品模型类'''
    ONLINE = 1
    OFFLINE = 0
    STATUS_CHOICE = {ONLINE:'上线',OFFLINE:'下线'}
    status_choices = ((k,v) for k,v in STATUS_CHOICE.items())

    type_id = models.ForeignKey(Type,verbose_name='商品种类')
    shop_name = models.ForeignKey(Shop,verbose_name='所属店铺')
    name = models.CharField(max_length=20,verbose_name ='商品名称')
    desc = models.CharField(max_length=128,verbose_name='主治功能')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='商品价格')
    unite = models.CharField(max_length=20,verbose_name='商品单位')
    stock = models.IntegerField(default=1,verbose_name='商品库存')
    sales = models.IntegerField(default=0,verbose_name='商品销量')
    detail = HTMLField(verbose_name='商品详情')
    image = models.ImageField(upload_to='goods',verbose_name='商品图片')
    status = models.SmallIntegerField(default=ONLINE,choices = status_choices,verbose_name='商品状态')
    objects = GoodsManager()

    class Meta:
        db_table = 'cm_goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
    def def__unicode__(self):
        return self.name

    def __str__(self):
        return self.name

