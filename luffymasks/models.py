from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True, blank=True)
    name = models.CharField(max_length = 200, null=True)
    email = models.CharField(max_length= 100, null=True)

    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length = 200, null=True, blank=True)
    price = models.FloatField(max_length = 200, null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True )
    image = models.ImageField(null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True )

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url= self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    name = models.CharField(max_length = 200, null=True)
    quantity = models.CharField(max_length = 200, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    product = models.ManyToManyField(product)
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank=True, null=True) 
    complete = models.BooleanField(default=False, null=True, blank=True )
    transaction_id = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return str(self.id)
    
   # @property
    #def shipping(self):
        #shipping = False
       # orderitems = self.orderitem_set.all(
       # for orderitem in orderitems:
           # if ordeeritem.product
       # )
       # return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum(orderitem.get_total for orderitem in orderitems)
        return total
        
    @property
    def get_cart_items_number(self):
        orderitems = self.orderitem_set.all()
        total = sum(orderitem.quantity for orderitem in orderitems)
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total

 

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length = 200, null=True)
    city = models.CharField(max_length = 200, null=True)
    state = models.CharField(max_length = 200, null=True)
    zipcode = models.CharField(max_length = 200, null=True)
    phone = models.IntegerField(max_length = 200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address