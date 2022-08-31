from django.contrib import admin
from .models import Attribute, AttributeValue, AttributeName, Image, Product, ProductAttributes, Catalog, ProductImage

# Register your models here.

admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(AttributeName)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(ProductAttributes)
admin.site.register(Catalog)
admin.site.register(ProductImage)

