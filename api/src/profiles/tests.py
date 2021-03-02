from django.test import TestCase
from rest_framework import status
from api.src.authentication.tests.base_test import BaseTest



class TestCustomerProfile(BaseTest):


    def test_can_list_all_profiles(self):
        res = self.client.get(
            self.CUSTOMER_PROFILES_URL,
            HTTP_AUTHORIZATION=self.access_token, 
            format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    

    def test_can_get_single_profile(self):
        res = self.client.get(
            self.CUSTOMER_PROFILES_URL+self.user_id+'/',
            HTTP_AUTHORIZATION=self.access_token, 
            format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_can_update_profile(self):
        res = self.client.patch(
        self.CUSTOMER_PROFILES_URL+self.user_id+'/',self.profile_update,
        HTTP_AUTHORIZATION=self.access_token, 
        format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_update_profile_fails(self):
        res = self.client.patch(
        self.CUSTOMER_PROFILES_URL+'4/',self.profile_update,
        HTTP_AUTHORIZATION=self.access_token, 
        format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
