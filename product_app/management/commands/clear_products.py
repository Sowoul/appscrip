from django.core.management.base import BaseCommand
from product_app.models import Product

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
