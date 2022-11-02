import json
from django.http import QueryDict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import ClassBelongsSerializer, ClassesSerializer, GetAttendanceSerializer, GetInfoSerializer, PostAttendanceSerializer, PostInfoSerializer, SubjectSerializer, TimeTableSerializer
from .models import Attendance, Classes, Subject, SubjectClassTeacherInfo, TimeTable

# Create your views here.


def data_return(data, data_name=None):
    if data_name:
        data_model = {"data": {data_name: data}}
    else:
        data_model = {"data": {data}}
    return data_model


def error_return(error):
    error_model = {"error": error}
    return error_model


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
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
                data_return(serializerSubject.data, 'subject'), status=status.HTTP_201_CREATED
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


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
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
            return Response(data_return(serializer.data, 'class'), status=status.HTTP_201_CREATED)
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
            serializer = GetInfoSerializer(info)
            return Response(
                data_return(serializer.data, "info"), status=status.HTTP_200_OK
            )
        else:
            classes = SubjectClassTeacherInfo.objects.all()
            serializer = GetInfoSerializer(classes, many=True)
            return Response(
                data_return(serializer.data, "info"), status=status.HTTP_200_OK
            )

    if request.method == "POST":
        serializer = PostInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data_return(serializer.data, 'info'), status=status.HTTP_201_CREATED)
        else:
            return Response(
                error_return(serializer.errors),
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    if id and request.method == "PUT" or id and request.method == "PATCH":
        serializer = PostInfoSerializer(info, data=data, partial=True)
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


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny])
def time_table(request, id=None):
    data = request.data
    if id:
        try:
            timetable = TimeTable.objects.get(pk=id)
        except:
            return Response(
                error_return([f"No data with {id}"]),
                status=status.HTTP_400_BAD_REQUEST,
            )
    if request.method == "GET":
        if id:
            serializer = TimeTableSerializer(timetable)
            return Response(
                data_return(serializer.data, "timetable"), status=status.HTTP_200_OK
            )
        else:
            classes = TimeTable.objects.all()
            serializer = TimeTableSerializer(classes, many=True)
            return Response(
                data_return(serializer.data, "timetable"), status=status.HTTP_200_OK
            )

    if request.method == "POST":
        serializer = TimeTableSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data_return(serializer.data, 'timetable'), status=status.HTTP_201_CREATED)
        else:
            return Response(
                error_return(serializer.errors),
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    if id and request.method == "PUT" or id and request.method == "PATCH":
        serializer = TimeTableSerializer(timetable, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data_return(serializer.data, "timetable"))
        return Response(
            error_return(serializer.errors), status=status.HTTP_202_ACCEPTED
        )

    if id and request.method == "DELETE":
        timetable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(error_return("wrong_request"))


def attend(data, cla, sub):
    info = SubjectClassTeacherInfo.objects.filter(classes=cla).get(subject=sub)
    attendance = Attendance.objects.filter(subject_class_teacher_info=info.id)
    timetable = TimeTable.objects.filter(subject_class_teacher_info=info.id)
    for i in timetable:
        if i.is_editable(attendance, data['date']):
            data.update({'subject_class_teacher_info': info.id})
            serializer = PostAttendanceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data_return(serializer.data, 'attendance'), status=status.HTTP_201_CREATED)
        else:
            return Response(
                error_return({'date': 'non_editable_at_this_time'}),
                status=status.HTTP_400_BAD_REQUEST,
            )

@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny])
def attendance(request, cla=None, sub=None):
    data = request.data
    if request.method == "GET":
        if cla and sub:
            info = SubjectClassTeacherInfo.objects.filter(classes=cla).get(subject=sub)
            attendance = Attendance.objects.filter(subject_class_teacher_info=info.id)
            serializer = GetAttendanceSerializer(attendance, many=True)
            return Response(
                data_return(serializer.data, "attendance"), status=status.HTTP_200_OK
            )
        else:
            classes = Attendance.objects.all()
            serializer = GetAttendanceSerializer(classes, many=True)
            return Response(
                data_return(serializer.data, "attendance"), status=status.HTTP_200_OK
            )

    if request.method == "POST":
        if cla and sub:
            if type(data) == list:
                for i in range(len(data)):
                    return attend(data[i], cla, sub)
            else:
                return attend(data, cla, sub)
        else:
            return Response(
                error_return(serializer.errors),
                status=status.HTTP_400_BAD_REQUEST,
            )


