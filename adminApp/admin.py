from django.contrib import admin
from .models import item_category,item,payment

# Register your models here.
class item_categoryAdmin(admin.ModelAdmin):
    list_display = ("id",'item_category_name','item_category_image')

class itemAdmin(admin.ModelAdmin):
    list_display = ('id','item_name','item_material','item_brand'
                    ,'item_price','item_dimension','item_colour',
                    "item_image1","item_image2","item_image3",'category')
    
class paymentAdmin(admin.ModelAdmin):
    list_display = ('id','name','card_no','cvv','expiry','balance')


admin.site.register(item_category,item_categoryAdmin)
admin.site.register(item,itemAdmin)
admin.site.register(payment,paymentAdmin)