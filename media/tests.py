"""Testing cases for the core app"""
import tempfile
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED
from PIL import Image
# Create your tests here.

class MediaTest(APITestCase):
    """Tests for login"""
    def test_upload_image(self):
        """Test a correct login"""
        
        url = reverse('upload')
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)

        data = {
            'file': tmp_file
        }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(HTTP_201_CREATED, response.status_code)

