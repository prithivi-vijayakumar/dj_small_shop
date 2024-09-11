from rest_framework import serializers

from backend.models import Category, Brand, Product, Order, Cart, CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
            customer_name = serializers.SerializerMethodField()
            product_id = serializers.SerializerMethodField()
            product_name = serializers.SerializerMethodField()
            product_image = serializers.SerializerMethodField()
            price = serializers.SerializerMethodField()

            class Meta:
                model = Cart
                fields = '__all__'

            def get_customer_name(self, obj):
                return obj.custom_user.email if obj.custom_user else None

            def get_product_id(self, obj):
                return obj.product.id if obj.product else None

            def get_product_name(self, obj):
                return obj.product.name if obj.product else None

            def get_product_image(self, obj):
                if obj.product and obj.product.images.exists():
                    request = self.context.get('request')
                    image_url = obj.product.images.first().image.url
                    return request.build_absolute_uri(image_url) if request else image_url
                return None

            # 'product_image']

            # def get_product_image(self, obj):
            #     request = self.context.get('request')
            #     if request is not None:
            #         return request.build_absolute_uri(obj.product.image.url)
            #     return obj.product.image.url

            def get_price(self, obj):
                return obj.product.price if obj.product else None

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'gender',
            'password',
            'email'
        ]

    def create(self, validated_data):
        user = super(CustomUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        # group = Group.objects.get(name='EMPLOYEE')
        # user.groups.add(group)
        user.is_staff = True
        user.is_active = True
        user.save()
        return user