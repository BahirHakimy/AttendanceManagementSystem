import json
from django.http import QueryDict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import ClassBelongsSerializer, ClassesSerializer, SubjectSerializer
from .models import Classes, Subject

# Create your views here.


def data_return(data, data_name=None):
    data_model = {"data": {data_name: data}}
    return data_model


def error_return(error):
    error_model = {"error": error}
    return error_model


@api_view(["GET", "POST", "PUT", "PATCH"])
@permission_classes([AllowAny])
def subject(request, id=None):
    data = request.data
    if id:
        try:
            subject = Subject.objects.get(pk=id)
        except:
            return Response(error_return([f'No subject with {id}']), status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        # try:
        query = request.query_params.get("search")
        print(query)
        if id:
            serializer = SubjectSerializer(subject)
            return Response(data_return(serializer.data, "subject"), status=status.HTTP_200_OK)
        elif query:
            subjects = Subject.objects.filter(title__icontains=query)
            serializer = SubjectSerializer(subjects, many=True)
            return Response(data_return(serializer.data, "subject"), status=status.HTTP_200_OK)
        else:
            subjects = Subject.objects.all()
            serializer = SubjectSerializer(subjects, many=True)
            return Response(data_return(serializer.data, "subject"), status=status.HTTP_200_OK)
        # except:
        #     return Response(error_return([f'wrong_query {request.query_params.dict()}']), status= status.HTTP_400_BAD_REQUEST)

    if request.method == "POST":
        serializerSubject = SubjectSerializer(data=data)
        if serializerSubject.is_valid():
            serializerSubject.save()
            return Response(
                {"data": serializerSubject.data}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"error": serializerSubject.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    if id and request.method == "PUT" or id and request.method == "PATCH":
        serializer = SubjectSerializer(subject, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data_return(serializer.data, "subject"))
        return Response(error_return(serializer.errors), status=status.HTTP_202_ACCEPTED)

    if id and request.method == "DELETE":
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error_return('wrong_request'))


@api_view(["GET", "POST", "PUT", "PATCH"])
@permission_classes([AllowAny])
def classe(request, id=None):
    data = request.data
    if id:
        try:
            classe = Classes.objects.get(pk=id)
        except:
            return Response(error_return([f'No class with {id}']), status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        try:
            if id:
                serializer = ClassBelongsSerializer(classe)
                return Response(data_return(serializer.data, "class"), status=status.HTTP_200_OK)
            elif query != '':
                query = request.query_params["search"]
                classes = Classes.objects.filter(title__icontains=query)
                serializer = ClassesSerializer(
                    classes, many=True, status=status.HTTP_200_OK)
                return Response(data_return(serializer.data, "class"))
            else:
                classes = Classes.objects.all()
                serializer = ClassesSerializer(classes, many=True)
                return Response(data_return(serializer.data, "class"), status=status.HTTP_200_OK)
        except:
            return Response(error_return([f'wrong_query {request.query_params.dict()}']), status=status.HTTP_400_BAD_REQUEST)

    if request.method == "POST":
        serializer = ClassesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": serializer.data}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                error_return(serializer.data, 'class'), status=status.HTTP_400_BAD_REQUEST
            )

    if id and request.method == "PUT" or id and request.method == "PATCH":
        serializer = ClassesSerializer(classe, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data_return(serializer.data, "class"))
        return Response(error_return(serializer.errors), status=status.HTTP_202_ACCEPTED)
    if id and request.method == "DELETE":
        classe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error_return('wrong_request'))
