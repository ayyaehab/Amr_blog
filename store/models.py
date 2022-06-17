from django.db import models
from django.forms import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

CATEGORIES = [
    ('book', 'book'),
    ('laptop', 'laptop'),
    ('pc', 'pc'),
    ('shirt', 'shirt'),
    ('mug', 'mug'),
    ('laptop', 'laptop'),
    ('accessories', 'accessories'),
    ('offers', 'offers'),
]


class Category(models.Model):
    name = models.CharField(max_length=50, choices=CATEGORIES, default='')
    slug = models.SlugField(max_length=80, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=3000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    oldPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    product_information = models.TextField(max_length=3000, null=True, blank=True)
    productCondition = models.CharField(max_length=45, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='static/imgs/product/%Y/%m/%d', null=True, blank=True)
    thumbnail1 = models.ImageField(upload_to='static/imgs/product/%Y/%m/%d', null=True, blank=True)
    thumbnail2 = models.ImageField(upload_to='static/imgs/product/%Y/%m/%d', null=True, blank=True)
    thumbnail3 = models.ImageField(upload_to='static/imgs/product/%Y/%m/%d', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if not self.slug:
                self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


# class ProductImg(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     img = models.ImageField(upload_to='static/imgs/product', default=True)
#
#     @property
#     def imageURL(self):
#         try:
#             product = self.img.url
#
#         except:
#             product = ''
#
#         return product
#
#     def __str__(self):
#         return str(self.product)


class CheckOut(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)
    fullname = models.CharField(max_length=255)
    address = models.TextField(max_length=300)
    phone = models.CharField(max_length=11)
    whatsapp = models.CharField(max_length=11)
    city = models.CharField(max_length=60)
    notes = models.TextField(max_length=300, null=True, blank=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    products_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.id} {self.fullname}'

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    checkout = models.ForeignKey(CheckOut, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} {self.checkout}'

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


@property
def get_cart_items(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.quantity for item in orderitems])
    return total
