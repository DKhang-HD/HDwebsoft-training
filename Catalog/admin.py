from django.contrib import admin
from .models import Category, Product, ProductInstance
from django.contrib import admin
# Register your models here.


class MyProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "author", "price", "pub_date"]
    list_filter = ("name", "price")
    fieldsets = (
        ('Information', {'fields': ("type", "name")}),
        ('Detail', {'fields': ("picture", "price", ("author", "pub_date"))}),
    )


class MyProductInstanceAdmin(admin.ModelAdmin):
    model = ProductInstance
    list_display = ["product", "status", "due_back"]
    list_filter = ("status", "due_back")


# class MyProductInline(admin.TabularInline):
#     model = Product


# Must have Forein key
# class MyCategoryAdmin(admin.ModelAdmin):
#     model = Category
#     inlines = [MyProductInline]


admin.site.register(Category)
admin.site.register(Product, MyProductAdmin)
admin.site.register(ProductInstance, MyProductInstanceAdmin)
# admin.site.register(Category, MyCategoryAdmin)
