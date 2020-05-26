from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import FileSerializer

class FileView(APIView):

  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()

      my_json = json.dumps({
    	"list":{
    	"data":file_serializer.data
    	}
    	})
      form = {
    	"file":request.FILES['file'],
    	"json":my_json
      }
      return Response(data=form, status=status.HTTP_201_CREATED)
    
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)