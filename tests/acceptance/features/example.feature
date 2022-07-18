
Feature: Upload a pet image

    Scenario Outline: Upload a picture for a Cat
        Given I send a request with authentication and the image <file>
        When the authentication is correct and the image data is no over 5MB
        Then it should upload the image to the server and make it only avaible for the user.

        Examples: Images
        | file        | response         |
        | my_cat.jpg  | 201 Created      |
        | my_dog.png  | 201 Created      |

        Examples: Other file types
        | file        |   response       |
        | receipt.txt |  400 Bad request |
        | financ.xlsx |  400 Bad request |

