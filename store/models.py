from django.db import models
from .category import Category


# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    category=models.ForeignKey(Category , verbose_name='category',null=True,blank=True, on_delete=models.SET_NULL)
    description=models.CharField(max_length=200, default='',null=True,blank=True)
    image=models.ImageField(upload_to='store/media')

    class Meta:
        verbose_name_plural='product'

    def __str__(self):
        return self.name
    @staticmethod
    def get_all_products():
        return product.objects.all()



