from PIL import Image
from django.urls import reverse
from behave import given, when, then
from rest_framework.status import HTTP_201_CREATED
import tempfile, json

@given('I send a request with authentication and the image {file}')
def step_given_send_request_with_image(context):
    image = Image.new('RGB', (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(tmp_file)
    context.url = reverse('upload')
    context.body = {
        'image': image
    }

@when('the authentication is correct and the image data is no over 5MB')
def step_when_send_request_with_image(context):
    context.response = context.test.client.post(context.url, body=json.dumps(context.body))

@then('it should upload the image to the server and make it only avaible for the user')
def step_then_send_request_with_image(context):
    context.test.assertEquals(context.response.status_code, HTTP_201_CREATED)
