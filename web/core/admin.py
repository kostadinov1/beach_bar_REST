from django.contrib import admin

# Register your models here.
from web.core.models import Event, ProductCategory, Product, PhotoGallery, PromoEvent


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(PromoEvent)
class PromoEventAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    pass




