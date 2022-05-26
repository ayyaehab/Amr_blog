from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=3000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='static/imgs/book', default=True)
    productCondition = models.CharField(max_length=45)
    slug = models.SlugField(null=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args,**kwargs)

    def __str__(self):
        return str(self.title)


class Mug(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=3000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20)
    productCondition = models.CharField(max_length=45)
    slug = models.SlugField(null=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Mug, self).save(*args,**kwargs)
    def __str__(self):
        return str(self.title)


class MugImg(models.Model):
    mug = models.ForeignKey(Mug, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/imgs/mug', default=True)

    def __str__(self):
        return str(self.mug)


class Tshirt(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=3000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20)

    brand = models.CharField(max_length=20)
    product_information = models.TextField(max_length=3000)
    productCondition = models.CharField(max_length=45)
    slug = models.SlugField(null=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Tshirt, self).save(*args,**kwargs)

    def __str__(self):
        return str(self.title)


class TshirtImg(models.Model):
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/imgs/shirt', default=True)

    def __str__(self):
        return str(self.tshirt)


class Pc(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=3000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=20)
    product_information = models.TextField(max_length=3000)
    productCondition = models.CharField(max_length=45)
    slug = models.SlugField(null=True, blank=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Pc, self).save(*args,**kwargs)

    def __str__(self):
        return str(self.title)


class PcImg(models.Model):
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/imgs/pc', default=True)

    def __str__(self):
        return str(self.pc)


class LapTop(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=3000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=20)
    product_information = models.TextField(max_length=3000)
    productCondition = models.CharField(max_length=45)
    slug = models.SlugField(null=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(LapTop, self).save(*args,**kwargs)
    def __str__(self):
        return str(self.title)


class LapTopImg(models.Model):
    lapTop = models.ForeignKey(LapTop, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/imgs/laptop', default=True)

    def __str__(self):
        return str(self.lapTop)
