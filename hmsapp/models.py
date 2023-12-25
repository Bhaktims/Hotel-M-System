from django.db import models

# Create your models here.
class Bookorder(models.Model):
    foodname=(('1',"Punjabi"),('2',"Maharashtrian"),('3',"South Indian"),('4',"Chinese"),('5',"Biryani"))
    cat=(('1',"Veg"),('2',"Non-veg"))
    
    foodname=models.CharField(max_length=50,verbose_name="Food Name",choices=foodname)
    qty=models.IntegerField(verbose_name="Qty")
    cat=models.CharField(max_length=50,verbose_name="Category",choices=cat)
    name=models.CharField(max_length=50,verbose_name="Customer")
    address=models.CharField(max_length=150)
    contact=models.BigIntegerField()
    uid=models.IntegerField()

    def __str__(self):
        return self.foodname
    
class Menu(models.Model):
    
    foodname=models.CharField(max_length=50)
    qty=models.IntegerField()
    cat=models.CharField(max_length=50,verbose_name="category")
    price=models.FloatField()
    stat=models.CharField(max_length=50,verbose_name="Status") 
       
    def __str__(self):
        return self.foodname
   
