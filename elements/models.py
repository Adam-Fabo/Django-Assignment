from django.db import models

# Create your models here.

class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=100, blank=True)


class AttributeName(models.Model):
    nazev = models.CharField(max_length=100, blank=True)
    kod = models.CharField(max_length=100, blank=True)
    zobrazit = models.BooleanField(null=True, blank=True)


class Attribute(models.Model):
    nazev_atributu_id  = models.ForeignKey(AttributeName, on_delete=models.DO_NOTHING)
    hodnota_atributu_id =  models.ForeignKey(AttributeValue, on_delete=models.DO_NOTHING)


class Image(models.Model):
    obrazek = models.URLField(max_length=1000,blank=True)


class Product(models.Model):
    nazev = models.CharField(max_length = 100, blank=True)
    description = models.TextField(max_length= 1000, blank=True)
    cena = models.IntegerField()
    mena = models.CharField(max_length = 20, blank=True)
    is_published = models.BooleanField(null=True, blank=True)


class ProductAttributes(models.Model):
    attribute  = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)
    product =  models.ForeignKey(Product, on_delete=models.DO_NOTHING)


class Catalog(models.Model):
    nazev = models.CharField(max_length=100, blank=True)
    obrazek_id = models.IntegerField(null=True, blank=True)

    products_ids = models.ManyToManyField(Product,blank=True)
    attributes_ids = models.ManyToManyField(Attribute,blank=True)


class ProductImage(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    obrazek_id =  models.ForeignKey(Image, on_delete=models.DO_NOTHING)

    nazev = models.CharField(max_length= 100, blank=True)





