from behave import when


@when("the authentication is correct and the image data is no over 5MB")
def step_when_send_request_with_image(context):
    context.response = context.test.client.post(context.url, context.body)


@when("the authentication is correct and the data is not an image")
def step_when_send_request_without_an_image(context):
    context.response = context.test.client.post(context.url, context.body)
