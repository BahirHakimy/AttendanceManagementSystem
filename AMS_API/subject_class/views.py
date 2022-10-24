from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import SubjectSerializer

# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def addSubject(request):
    data = request.data
    serializerSubject = SubjectSerializer(data=data)
    if serializerSubject.is_valid():
        serializerSubject.save()
        return Response({'data': serializerSubject.data}, status=status.HTTP_201_CREATED)
    else:
        return  Response({'error': serializerSubject.errors}, status= status.HTTP_400_BAD_REQUEST)

