import json
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .models import UploadImage
from .serialziers import ImageSerializer

# Create your views here.


class ImageViewSet(ListAPIView):
    queryset = UploadImage.objects.all()
    serializer_class = ImageSerializer

    def post(self, request):
        file = request.data["file"]
        image = UploadImage.objects.create(image=file)
        image_relative = str(image.image)
        return HttpResponse(json.dumps({"route": str(image_relative)}), status=201)
