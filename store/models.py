from datetime import datetime

from django.db import models
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify
from django.views import View


class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False


class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    oldPrice = models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True)
    brand = models.CharField(max_length=20,null=True, blank=True)
    product_information = models.TextField(max_length=3000,null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')
    color = models.CharField(max_length=20, blank=True, null=True)
    productCondition = models.CharField(max_length=45, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.name)


@staticmethod
def get_products_by_id(ids):
    return Products.objects.filter(id__in=ids)


@staticmethod
def get_all_products():
    return Products.objects.all()


@staticmethod
def get_all_products_by_categoryid(category_id):
    if category_id:
        return Products.objects.filter(category=category_id)
    else:
        return Products.get_all_products()


class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')






# from django.db import models
# from django.utils.text import slugify
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField(max_length=3000)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     oldPrice = models.DecimalField(max_digits=10, decimal_places=2)
#     img = models.ImageField(upload_to='static/imgs/book', default=True)
#     productCondition = models.CharField(max_length=45)
#     slug = models.SlugField(null=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Book, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.title)
#
#
# class Mug(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField(max_length=3000)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     oldPrice =models.DecimalField(max_digits=10, decimal_places=2)
#     color = models.CharField(max_length=20)
#     productCondition = models.CharField(max_length=45)
#     thumbnail = models.ImageField(upload_to='static/imgs/mug', default=True)
#     slug = models.SlugField(null=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Mug, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.title)
#
#
# class MugImg(models.Model):
#     mug = models.ForeignKey(Mug, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to='static/imgs/mug', default=True)
#
#     def __str__(self):
#         return str(self.mug)
#
#
# class Tshirt(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField(max_length=3000)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     oldPrice = models.DecimalField(max_digits=10, decimal_places=2)
#     color = models.CharField(max_length=20)
#
#     brand = models.CharField(max_length=20)
#     product_information = models.TextField(max_length=3000)
#     productCondition = models.CharField(max_length=45)
#     thumbnail = models.ImageField(upload_to='static/imgs/shirt', default=True)
#     slug = models.SlugField(null=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Tshirt, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.title)
#
#
# class TshirtImg(models.Model):
#     tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to='static/imgs/shirt', default=True)
#
#     def __str__(self):
#         return str(self.tshirt)
#
#
# class Pc(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField(max_length=3000)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     oldPrice = models.DecimalField(max_digits=10, decimal_places=2)
#     brand = models.CharField(max_length=20)
#     product_information = models.TextField(max_length=3000)
#     productCondition = models.CharField(max_length=45)
#     thumbnail = models.ImageField(upload_to='static/imgs/pc', default=True)
#     slug = models.SlugField(null=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Pc, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.title)
#
#
# class PcImg(models.Model):
#     pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to='static/imgs/pc', default=True)
#
#     def __str__(self):
#         return str(self.pc)
#
#
# class LapTop(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField(max_length=3000)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     oldPrice = models.DecimalField(max_digits=10, decimal_places=2)
#     brand = models.CharField(max_length=20)
#     product_information = models.TextField(max_length=3000)
#     productCondition = models.CharField(max_length=45)
#     thumbnail = models.ImageField(upload_to='static/imgs/laptop', default=True)
#
#     slug = models.SlugField(null=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(LapTop, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.title)
#
#
# class LapTopImg(models.Model):
#     lapTop = models.ForeignKey(LapTop, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to='static/imgs/laptop', default=True)
#
#     def __str__(self):
#         return str(self.lapTop)
#
# #
# # class Customer(models.Model):
# #     first_name = models.CharField(max_length=45)
# #     email = models.EmailField()
# #     password = models.CharField(max_length=45)
# #     address = models.CharField(max_length=45)
# #     city = models.CharField(max_length=45)
# #     state = models.CharField(max_length=45)
# #     phone_number = models.CharField(max_length=11)
# #     phone_second_number = models.CharField(max_length=11)
# #     slug = models.SlugField(null=True, blank=True)
# #
# #     def save(self, *args, **kwargs):
# #         self.slug = slugify(self.first_name)
# #         super(Customer, self).save(*args, **kwargs)
# #
# #     def __str__(self):
# #         return str(self.first_name)
# #
# #
# # class Order(models.Model):
# #     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
# #     date = models.DateTimeField(auto_now_add=True)
# #     total = models.DecimalField(max_digits=10, decimal_places=2)
# #     slug = models.SlugField(null=True, blank=True)
# #
# #     def save(self, *args, **kwargs):
# #         self.slug = slugify(self.customer)
# #         super(Order, self).save(*args, **kwargs)
# #
# #     def __str__(self):
# #         return str(self.customer)
# #
# #
# # class OrderItem(models.Model):
# #     product_Book = models.ForeignKey(Book, on_delete=models.CASCADE)
# #     product_LapTop = models.ForeignKey(LapTop, on_delete=models.CASCADE)
# #     product_Pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
# #     product_Tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
# #     product_Mug = models.ForeignKey(Mug, on_delete=models.CASCADE)
# #     order = models.ForeignKey(Order, on_delete=models.CASCADE)
# #     quantity = models.IntegerField(default=0, null=True, blank=True)
# #     date_added = models.DateTimeField(auto_now_add=True)
# #
# #     @property
# #     def get_total(self):
# #         total = self.product.price * self.quantity
# #         return total
# #
# #
# # class ShippingAddress(models.Model):
# #     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
# #     order = models.ForeignKey(Order, on_delete=models.CASCADE)
# #     address = models.CharField(max_length=200, null=False)
# #     city = models.CharField(max_length=200, null=False)
# #     state = models.CharField(max_length=200, null=False)
# #     zipcode = models.CharField(max_length=200, null=False)
# #     date_added = models.DateTimeField(auto_now_add=True)
# #
# #     def __str__(self):
# #         return self.address
