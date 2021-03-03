from rest_framework import status
from api.src.authentication.tests.base_test import BaseTest

class OrdersTests(BaseTest):
    def test_can_get_all_orders(self):
        res= self.client.get(self.ORDERS_LIST_URL,format="json")
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_can_get_an_orders(self):
        res= self.client.get(self.ORDERS_RETRIEVE_URL+"24/",format="json")
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_can_creat_an_orders(self):
        data = {
            "item_name": "Delmonte Apple Flavour",
            "amount": 205.00,
            "customer": int(self.user_id)
        }
        res= self.client.post(self.ORDERS_CREATE_URL,
        data,HTTP_AUTHORIZATION=self.access_token,format="json")
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
