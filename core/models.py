from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
# from distutils.command.upload import upload
from taggit.managers import TaggableManager

STATUS_CHOICE = (
    ("process", "Processing"),
    ("delivered", "Delivered"),
)
STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In_Review"),
    ("published", "Published"),
)
RATING = (
    (1, "✯✰✰✰✰"),
    (2, "✯✯✰✰✰"),
    (3, "✯✯✯✰✰"),
    (4, "✯✯✯✯✰"),
    (5, "✯✯✯✯✯"),
)


# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix='category', alphabet="abcdefghij")
    title = models.CharField(max_length=100, default="Category Title")
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.image.url)

    def __str__(self):
        return self.title


class Tags(models.Model):
    pass


class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=30, prefix='vendor', alphabet="abcdefghij")
    title = models.CharField(max_length=100, default="Vendor title")
    image = models.ImageField(upload_to="vendor", default="vendor.jpg")
    cover_image = models.ImageField(upload_to="vendor", default="vendor.jpg")
    description = models.TextField(null=True, blank=True, default="This is the vendor description")
    address = models.CharField(max_length=100, default="Nairobi")
    contact = models.CharField(max_length=100, default="0712345678")
    chat_response_time = models.CharField(max_length=100, default="100")
    delivery_on_time = models.CharField(max_length=100, default="100")
    authenticity_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.image.url)

    def vendor_cover_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.cover_image.url)

    def __str__(self):
        return self.title


class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=30, prefix='product', alphabet="abcdefghij")
    title = models.CharField(max_length=100, default="Product title")
    image = models.ImageField(upload_to="user_directory_path", default="product.jpg")
    description = models.TextField(null=True, blank=True, default="This is the product description")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name="vendor_product")

    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default=0.00)
    old_price = models.DecimalField(max_digits=999999999999, decimal_places=2, default=0.00)
    specifications = models.TextField(null=True, blank=True, default="This is the product specifications")
    stock_count = models.CharField(max_length=100, default="10")
    life = models.CharField(max_length=100, default="10")
    manufacture_date = models.DateTimeField(null=True, blank=True, auto_now_add=False)

    tags = TaggableManager(blank=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=5, max_length=30, prefix='sku', alphabet="1234567890")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.image.url)

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price


class ProductImages(models.Model):
    images = models.ImageField(upload_to="product_images", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="product_images")
    # product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

    def product_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % self.images.url)


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

    class Meta:
        verbose_name_plural = "Cart Order"


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=200)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999999, decimal_places=2, default="0.00")
    total = models.DecimalField(max_digits=9999999999, decimal_places=2, default="0.00")

    class Meta:
        verbose_name_plural = "Cart Order Items"

    def order_image(self):
        return mark_safe('<img src="/media/%s" width="40" height="40" />' % self.image)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wishlists"

    def __str__(self):
        return self.product.title


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"
