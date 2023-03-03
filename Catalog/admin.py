from django.contrib import admin
from .models import Category, Product, ProductInstance
from django.contrib import admin
# Register your models here.


class MyProductInline(admin.TabularInline):
    model = ProductInstance
    extra = 0
    readonly_fields = ('id', )
    can_delete = False


class MyProductInstanceAdmin(admin.ModelAdmin):
    model = ProductInstance
    list_display = ["product", "status", "due_back"]
    list_filter = ("status", "due_back")


class MyProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "author", "price", "pub_date"]
    list_filter = ("name", "price")
    fieldsets = (
        ('Information', {'fields': ("type", "name")}),
        ('Detail', {'fields': ("picture", "price", ("author", "pub_date"))}),
    )

    inlines = [MyProductInline]




# Must have Forein key
# class MyCategoryAdmin(admin.ModelAdmin):
#     model = Category
#     inlines = [MyProductInline]


admin.site.register(Category)
admin.site.register(Product, MyProductAdmin)
admin.site.register(ProductInstance, MyProductInstanceAdmin)
# admin.site.register(Category, MyCategoryAdmin)
