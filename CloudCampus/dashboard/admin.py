from django.contrib import admin
from .models import AcademicYear, Course, Subject, Semester, Student, Attendence, Hours, TimeTable, Weekday, AdminProfile, Notification, NotificationStudent,AttendenceFlag, SeminarAssignmentProject, Department, Teacher

admin.site.register(AcademicYear)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Attendence)
admin.site.register(Hours)
admin.site.register(TimeTable)
admin.site.register(Weekday)
admin.site.register(AdminProfile)
admin.site.register(Notification)
admin.site.register(NotificationStudent)
admin.site.register(SeminarAssignmentProject)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(AttendenceFlag)