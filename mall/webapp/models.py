from django.db import models
from django.urls import reverse

CHOICES = [('other', 'разное'), ('electronics', 'электроника'), ('clothes', 'одежда'), ('for_home', 'Для дома'),
           ('sports', 'спорт')]

class Stufs(models.Model):
    stuf = models.CharField(max_length=100, null=False, blank=True, verbose_name='stuf')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="description")
    categories = models.TextField(null=False, blank=True, choices=CHOICES,
                                  default=CHOICES[0][0],
                                  verbose_name="categories")
    remainder = models.PositiveIntegerField(null=False, blank=True, verbose_name="remainder")
    price = models.DecimalField(null=False, blank=True, max_digits=7, decimal_places=2, verbose_name="price")

    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.pk})

    def __str__(self):
        return f'| {self.stuf} | {self.description} | {self.categories} | {self.remainder} | {self.price} |'

class Stufs_in_cart(models.Model):
    stuf_key = models.ForeignKey('webapp.Stufs', on_delete=models.CASCADE, verbose_name='stuf_key', related_name='stuf_key')
    amount_stuf = models.PositiveIntegerField(verbose_name='amount_stuf', null=True, blank=True)

    def __str__(self):
        return f'{self.stuf_key} | {self.amount_stuf}'

    def total(self):
        return self.stuf_key.price * self.amount_stuf

class order(models.Model):
    user = models.CharField(max_length=40, verbose_name='user')
    numbers = models.CharField(max_length=50, verbose_name='numbers')
    adress = models.CharField(max_length=50, verbose_name='adress')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='date_c')

    def __str__(self):
        return f'{self.user}'

class Promej(models.Model):
    order = models.ForeignKey('webapp.order', related_name='order', on_delete=models.CASCADE, verbose_name='order')
    stufs = models.ForeignKey('webapp.Stufs', related_name='stufs', on_delete=models.CASCADE, verbose_name='stufs')

    def __str__(self):
        return f'{self.order}, {self.stufs}'