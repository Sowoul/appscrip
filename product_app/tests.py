from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client=APIClient()
        self.product=Product.objects.create(id=1,name="Test Product",description="Dummy Description",price=9.99,stock_quantity=10)

    def test_list_products(self):
        response = self.client.get('/api/products')
        self.assertEqual(response.status_code, 200)

    def test_get_single_product(self):
        response = self.client.get(f'/api/products/{self.product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Test Product")

    def test_create_product(self):
        data = {"id": 2,"name": "test product","description": "dummy", "price": 999.99, "stock_quantity": "5"}
        response = self.client.post('/api/products', data)
        self.assertEqual(response.status_code, 201)

    def test_update_product(self):
        data = {"id" : self.product.id,"name": "update", "description": "Updated", "price": 899.99, "stock_quantity": "7"}
        response = self.client.put(f'/api/products/{self.product.id}', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "update")

    def test_delete_product(self):
        response = self.client.delete(f'/api/products/{self.product.id}')
        self.assertEqual(response.status_code, 204)
