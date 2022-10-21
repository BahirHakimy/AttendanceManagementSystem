from .models import Teacher, Subject, Class, AttendanceForm, TimeTable

# Create your views here.


# def get_classes_for_teacher(request):
#     teacherUsername = request.data["teacher"]
#     subjectTitle = request.data["subject"]

#     teacher = Teacher.objects.get(username=teacherUsername)
#     subject = Subject.objects.get(title=subjectTitle)

#     return subject.get_classes_for_teacher(teacher)


# def get_attendance_form(request):
#     class_id = request.data.get("classID")
#     subject_id = request.data.get("subID")

#     subject = Subject.objects.get(id=subject_id)
#     class_object = Class.objects.get(id=class_id)
#     form = AttendanceForm.objects.get(parent_class=class_object, subject=subject)
