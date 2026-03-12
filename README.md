# CS361 (Group 17) - Big Pool Microservice: QR Code Generator

**What does this microservice do?**

This microservice allows the user to get a QR code for the provided link. Optionally, the user can provide the name of a brand and the QR code provided will include branding. Currently, only branding for `envite` is natively supported.. It will return a string representing the image in base64..

**How do I request data from this microservice?**

To request data from this microservice, you will need to make an `HTTP GET request` to the `/qrcode` endpoint. You must pass `url` as a string that represents the URL that the QR code will redirect to. You may optionally pass the `brand` as a string that represents the brand of the provided link as a query parameter.

_Example call:_ `GET http://127.0.0.1:8000/qrcode?url=google.com`

_Example call:_ `GET http://127.0.0.1:8000/qrcode?url=envite.com&brand=envite`


**How will I receive data from this microservice?**

The microservice will return a `JSON object`. The object will have one name/value pair. The name/value pair will be `base_64_image` which is a string representing an image in base64 format.

_Example response_:

Status code: `200`
```yaml
{
"base_64_image": <base64 string representing the image>
}
```
