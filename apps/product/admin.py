from django.contrib import admin

from .models import Category, Product, ProductImage, Rate,Category_name




class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class RateInline(admin.TabularInline):
    model = Rate
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,RateInline]


class CategoryAdmin(admin.ModelAdmin):

    list_filter = ('font_type', 'parent_category')
    list_display = ('id', 'name', 'parent_category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Rate)

admin.site.register(Category_name)
