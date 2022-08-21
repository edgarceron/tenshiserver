from behave import then
from rest_framework.status import HTTP_201_CREATED


@then(
    "it should upload the image to the server and it should response with a {status} code"
)
def step_then_send_request_with_image(context, status):
    context.test.assertEquals(context.response.status_code, int(float(status)))


@then(
    "it shouldn't upload the file to the server and it should response with a {status} code"
)
def step_then_send_request_without_an_image(context, status):
    context.test.assertEquals(context.response.status_code, int(float(status)))
