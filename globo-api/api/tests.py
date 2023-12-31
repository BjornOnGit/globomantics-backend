from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Inquiry

class InquiryTestCase(TestCase):
    """ Inquiry model test case"""
    @classmethod
    def setUpTestData(cls):
        cls.inquiry = Inquiry.objects.create(
            name = 'test name',
            email = 'test@example.com',
            remarks = 'test remarks'
        )
    
    def test_model_content(self):
        """ Test model content """
        self.assertEqual(self.inquiry.name, 'test name')
        self.assertEqual(self.inquiry.email, 'test@example.com')
        self.assertEqual(self.inquiry.remarks, 'test remarks')
    
    def test_api_createview(self):
        """ Test InquiryCreateView"""
        Inquiry.objects.all().delete()
        data = {
            'name': 'test name',
            'email': 'test@example.com',
            'remarks': 'test remarks',
        }
        response = self.client.post(reverse('inquiry_list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inquiry.objects.count(), 1)
        self.assertEqual(response.data['name'], 'test name')
    
    def test_api_detailview(self):
        """Test InquiryDetailView"""
        response = self.client.get(reverse('inquiry_detail', kwargs={'pk': self.inquiry.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Inquiry.objects.count(), 1)
        self.assertContains(response, 'test name')

# Create your tests here.
