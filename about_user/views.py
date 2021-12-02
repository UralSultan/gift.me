
from rest_framework import views, response, status

from .serializer import AboutSerializers


class AboutUserAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = AboutSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
