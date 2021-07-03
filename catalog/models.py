from django.db import models
from django.urls import reverse
from category.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    public_price = models.DecimalField(max_digits=9, decimal_places=2)
    internal_price = models.DecimalField(max_digits=9, decimal_places=2,
                                    blank=True, default=0.00)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    is_available = models.BooleanField(default=True)
    quantity = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expire_at = models.DateTimeField()

    class Meta:
        db_table = 'products'
        ordering = ['-created_at', 'name']
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None

    def get_absolute_url(self):
        return reverse('catalog:product_detail',
                       args=[self.id, self.slug])
