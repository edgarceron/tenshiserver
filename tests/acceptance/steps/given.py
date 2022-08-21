import tempfile

from behave import given
from django.urls import reverse
from PIL import Image


@given("I send a request with authentication and the image {file}")
def step_given_send_request_with_image(context, file: str):
    image = Image.new("RGB", (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg", prefix=file)
    image.save(tmp_file, "jpeg")
    context.url = reverse("upload")
    context.body = {"file": image}


@given("I send a request without a valid image {file}")
def step_given_send_request_without_an_image(context, file: str):
    tmp_file = tempfile.NamedTemporaryFile(suffix=".txt", prefix=file)
    context.url = reverse("upload")
    context.body = {"file": tmp_file}
