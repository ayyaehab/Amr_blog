import django_filters

from store.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = '__all__'
        exclude =['thumbnail','created']
