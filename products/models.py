from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class BaseItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta :
        abstract = True

class CategoryProduct(BaseItem):
    def __str__(self):
        return self.name

class Product(BaseItem):
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False,validators=[MinValueValidator(0)])
    price_old = models.DecimalField(max_digits=10,decimal_places=2,null=True,validators=[MinValueValidator(0)],blank=True)
    quantity = models.PositiveIntegerField(default=1000)
    amount_sold = models.PositiveIntegerField(default=0)
    hot = models.BooleanField(default=False)
    category = models.ForeignKey(CategoryProduct,on_delete=models.PROTECT)
    image = models.CharField(max_length=255,default="https://salt.tikicdn.com/cache/400x400/media/catalog/producttmp/5c/6a/ca/140ee956b63c166c73407bd1becda03c.jpg.webp")
    def __str__(self):
        return self.name

class Rating(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False,related_name="product_rate")
    creator = models.ForeignKey('users.UserCustom', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(default=0,validators=[MaxValueValidator(5)])
    des = models.TextField(default='',null= True,blank=True)
    def __str__(self):
        return self.product.name