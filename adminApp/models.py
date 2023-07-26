from django.db import models

# Create your models here.
class item_category(models.Model):
    item_category_name = models.CharField(max_length=50)
    item_category_image = models.ImageField(upload_to='images',default='abc.jpg')

    def __str__(self):
        return self.item_category_name

    class Meta:
        db_table = "category"

class item(models.Model):
    item_name = models.CharField(max_length=200)
    item_material = models.CharField(max_length=200)
    item_colour = models.CharField(max_length=200)
    item_brand = models.CharField(max_length=200)
    item_price = models.FloatField(max_length=200)
    item_dimension = models.CharField(max_length=200)
    item_image1 = models.ImageField(upload_to='images',default='abc.jpg')
    item_image2 = models.ImageField(upload_to='images',default='abc.jpg')
    item_image3 = models.ImageField(upload_to='images',default='abc.jpg')

    category = models.ForeignKey(item_category,on_delete=models.CASCADE) 

    class Meta:
        db_table = 'items'
    
class payment(models.Model):
    name = models.CharField(max_length=50,default='xyz')
    card_no = models.CharField(max_length=5)
    cvv = models.CharField(max_length=5)
    expiry = models.CharField(max_length=10)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = 'payment'
