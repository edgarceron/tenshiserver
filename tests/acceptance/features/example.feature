
Feature: Upload a pet image

    Scenario Outline: Upload a picture for a Cat
        Given I send a request with authentication and the image <file>
        When the authentication is correct and the image data is no over 5MB
        Then it should upload the image to the server and it should response with a <status> code

        Examples:
        | file        | status |
        | my_cat.jpg  | 201    |
        | my_dog.png  | 201    |


    Scenario Outline: Fail upload a picture for a Cat
        Given I send a request without a valid image <file>
        When the authentication is correct and the data is not an image
        Then it shouldn't upload the file to the server and it should response with a <status> code

        Examples:
        | file             | status |
        | not_an_image.txt | 401    |
        | not_an_image.txt | 401    |


