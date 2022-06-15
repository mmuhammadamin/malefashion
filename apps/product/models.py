from django.contrib.auth.models import User
from django.db import models


class Timestamp(models.Model):
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.

class Category(Timestamp):
    FONT_TYPE = (
        (0, 'text'),
        (1, 'square'),
        (2, 'circle'),
        (3, 'tag'),
        (4, 'parent node'),

    )
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                        limit_choices_to={'font_type': 4})
    font_type = models.IntegerField(choices=FONT_TYPE, default=4)

    @property
    def normalize_title(self):
        return self.name.replace(' ', '').lower()

    def __str__(self):
        return self.name


class Category_name(models.Model):
    category_title = models.CharField(max_length=100)

    def __str__(self):
        return self.category_title


class Product(Timestamp):
    category = models.ForeignKey(Category_name, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=220)
    price = models.FloatField()
    mid_rate = models.FloatField()
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True)
    condition = models.CharField(max_length=20, blank=True)
    category_shop = models.ManyToManyField(Category, limit_choices_to={'font_type__lt': 4})


    @property
    def normalize_title(self):
        return self.name.replace(' ', '').lower()

    def __str__(self):
        return self.name

    @property
    def get_mid_rate(self):
        rates = self.rate_set.all()
        mid = 0
        try:
            mid = sum([i.rate for i in rates]) / rates.count()
        except ZeroDivisionError:
            pass
        self.mid_rate = mid
        self.save()
        return mid


class ProductImage(Timestamp):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return f'image of {self.product}'


class Rate(Timestamp):
    Rate = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.IntegerField()


    def __str__(self):
        return f'Rate of {self.user.username}'


