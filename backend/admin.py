from django.contrib import admin

from django.utils.html import format_html
from backend.models import CustomUser, Category, Brand, Product, Cart, Order, OrderItem

from django.contrib.auth.admin import UserAdmin
from backend.forms import CustomerUserCreationForm,CustomerUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display = ('email','gender','image_tag','is_staff','is_active',)
    list_filter = ('email','is_staff','is_active',)
    fieldsets = (
        (None,{'fields': ('email','gender','password')}),
        ('Permissions',{'fields':('is_staff','is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','gender','password1','password2','is_staff','is_active', 'groups', 'user_permissions')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    def image_tag(self,obj):
        return format_html('<img src = "{}"width="150" height="150"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

admin.site.register(CustomUser,CustomUserAdmin)

class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id','name')


admin.site.register(Category,CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag',)

    def image_tag(self, obj):
        return format_html('<img src = "{}" width = "150" height="150" />'.format(obj.image_path.url))

    image_tag.short_description = 'Image'


admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','brand','price','qty','name','image_tag',)

    def image_tag(self, obj):
        return format_html('<img src = "{}" width = "150" height="150" />'.format(obj.image_path.url))

    image_tag.short_description = 'Image'


admin.site.register(Product,ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', 'Product', 'qty',)


admin.site.register(Cart, CartAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'custom_user', 'order_number', 'order_date', 'total_amount', 'order_status', 'payment_method',)
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)