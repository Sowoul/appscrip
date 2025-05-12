from django.core.management.base import BaseCommand
from product_app.tasks.import_products import import_products

class Command(BaseCommand):
    help = 'Import products from static JSON or fakestoreapi.com'

    def handle(self, *args, **kwargs):
        try:
            import_products()
            self.stdout.write(self.style.SUCCESS("Products imported successfully!"))
        except Exception as e:
            self.stderr.write(str(e))
