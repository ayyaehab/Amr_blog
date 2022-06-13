from django.db import models
from django.forms import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
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
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=3000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    oldPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    product_information = models.TextField(max_length=3000, null=True, blank=True)
    productCondition = models.CharField(max_length=45, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='static/imgs/product/%Y/%m/%d', default=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/imgs/product', default=True)

    @property
    def imageURL(self):
        try:
            product = self.img.url

        except:
            product = ''

        return product

    def __str__(self):
        return str(self.product)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


@property
def get_cart_items(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.quantity for item in orderitems])
    return total


Counties_CHOICES = [
    ('egypt', 'Egypt'),
    ('alex', 'Alexandria')
]


class CheckOut(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=60)
    area = models.CharField(default='ما هي محافظتك ؟', choices=Counties_CHOICES, max_length=6)
    country = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    whats_number = models.CharField(max_length=11)
    notes = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.name)
