import json
from django.http import QueryDict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import ClassBelongsSerializer, ClassesSerializer, InfoSerializer, SubjectSerializer
from .models import Classes, Subject, SubjectClassTeacherInfo

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
            return Response(
                error_return([f"No subject with {id}"]),
                status=status.HTTP_400_BAD_REQUEST,
            )
    if request.method == "GET":
        try:
            query = request.query_params
            if id:
                serializer = SubjectSerializer(subject)
                return Response(
                    data_return(serializer.data, "subject"), status=status.HTTP_200_OK
                )
            elif len(query):
                query = query["search"]
                subjects = Subject.objects.filter(title__icontains=query)
                serializer = SubjectSerializer(subjects, many=True)
                return Response(
                    data_return(serializer.data, "subject"), status=status.HTTP_200_OK
                )
            else:
                subjects = Subject.objects.all()
                serializer = SubjectSerializer(subjects, many=True)
                return Response(
                    data_return(serializer.data, "subject"), status=status.HTTP_200_OK
                )
        except:
            return Response(
                error_return([f"wrong_query {request.query_params.dict()}"]),
                status=status.HTTP_400_BAD_REQUEST,
            )

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
        return Response(
            error_return(serializer.errors), status=status.HTTP_202_ACCEPTED
        )

    if id and request.method == "DELETE":
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error_return("wrong_request"))


@api_view(["GET", "POST", "PUT", "PATCH"])
@permission_classes([AllowAny])
def classe(request, id=None):
    data = request.data
    if id:
        try:
            classe = Classes.objects.get(pk=id)
        except:
            return Response(
                error_return([f"No class with {id}"]),
                status=status.HTTP_400_BAD_REQUEST,
            )
    if request.method == "GET":
        query = request.query_params
        try:
            if id:
                serializer = ClassBelongsSerializer(classe)
                return Response(
                    data_return(serializer.data, "class"), status=status.HTTP_200_OK
                )
            elif len(query):
                query = query["search"]
                classes = Classes.objects.filter(name__icontains=query)
                serializer = ClassesSerializer(classes, many=True)
                return Response(
                    data_return(serializer.data, "class"), status=status.HTTP_200_OK
                )
            else:
                classes = Classes.objects.all()
                serializer = ClassesSerializer(classes, many=True)
                return Response(
                    data_return(serializer.data, "class"), status=status.HTTP_200_OK
                )
        except:
            return Response(
                error_return([f"wrong_query {request.query_params.dict()}"]),
                status=status.HTTP_400_BAD_REQUEST,
            )

    if request.method == "POST":
        serializer = ClassesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                error_return(serializer.errors, "class"),
                status=status.HTTP_400_BAD_REQUEST,
            )

    if id and request.method == "PUT" or id and request.method == "PATCH":
        serializer = ClassesSerializer(classe, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data_return(serializer.data, "class"))
        return Response(
            error_return(serializer.errors), status=status.HTTP_202_ACCEPTED
        )
    if id and request.method == "DELETE":
        classe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error_return("wrong_request"))


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny])
def subject_class_info(request, id=None):
    data = request.data
    if id:
        try:
            info = SubjectClassTeacherInfo.objects.get(pk=id)
        except:
            return Response(
                error_return([f"No info with {id}"]),
                status=status.HTTP_400_BAD_REQUEST,
            )
    if request.method == "GET":
        if id:
            serializer = InfoSerializer(info)
            return Response(
                data_return(serializer.data, "info"), status=status.HTTP_200_OK
            )
        else:
            classes = SubjectClassTeacherInfo.objects.all()
            serializer = InfoSerializer(classes, many=True)
            return Response(
                data_return(serializer.data, "info"), status=status.HTTP_200_OK
            )

    if request.method == "POST":
        serializer = InfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                error_return(serializer.errors),
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    if id and request.method == "PUT" or id and request.method == "PATCH":
        serializer = InfoSerializer(info, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data_return(serializer.data, "info"))
        return Response(
            error_return(serializer.errors), status=status.HTTP_202_ACCEPTED
        )

    if id and request.method == "DELETE":
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error_return("wrong_request"))