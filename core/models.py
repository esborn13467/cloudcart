from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

from userauths.models import User


# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix='category', alphabet=abcdefghij)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="{self.image.url}" width="40" height="40" />')

    def __str__(self):
        return self.title


class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=30, prefix='vendor', alphabet=abcdefghij)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="vendor")
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100, default="Nairobi")
    contact = models.CharField(max_length=100, default="0712345678")
    chat_response_time = models.CharField(max_length=100, default="100")
    delivery_on_time = models.CharField(max_length=100, default="100")
    authenticity_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="{self.image.url}" width="40" height="40" />')

    def __str__(self):
        return self.title