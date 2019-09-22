from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
import datetime
from datetime import datetime
from datetime import date
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import AcademicYear, Course, Subject, Semester, Department, Student, Hours, Attendence, AdminProfile, Notification, NotificationStudent, SeminarAssignmentProject, Teacher, AttendenceFlag
# Create your views here.

@login_required
def dashboard(request):
	usrprof = UserProfile.objects.get(user=request.user)
	if usrprof.is_admin == True:
		admin = AdminProfile.objects.get(id=1)
		students_count = Student.objects.all().count()
		notification = Notification.objects.all()
		todays = date.today
		course_count = Course.objects.all().count()
		teacher_count = Teacher.objects.all().count()
		students_count = Student.objects.all().count()
		return render(request, 'dashboard/index-admin.html', {'admins':admin, 'students_counts':students_count, 'notifications':notification, 'today':todays, 'teacher_count':teacher_count, 'students_count': students_count, 'course_count': course_count})

	if usrprof.is_teacher == True:
		usrprof = UserProfile.objects.get(user=request.user)

		teacher_now = Teacher.objects.get(teacher_id = usrprof.uid)
		students_count = Student.objects.all().count()
		notification = Notification.objects.all()
		todays = date.today
		course_count = Course.objects.all().count()
		teacher_count = Teacher.objects.all().count()
		students_count = Student.objects.all().count()
		cnotification = NotificationStudent.objects.all()
		return render(request, 'dashboard/index-teacher.html', {'admins':usrprof, 'teacher':teacher_now, 'students_counts':students_count, 'notifications':notification,'cnotifications':cnotification, 'today':todays, 'teacher_count':teacher_count, 'students_count': students_count, 'course_count': course_count})

	if usrprof.is_student == True:
		students_count = Student.objects.all().count()
		notification = Notification.objects.all()
		notificationstu = NotificationStudent.objects.all()
		notification_count = NotificationStudent.objects.all().count()
		student_now = Student.objects.get(roll_number = usrprof.uid)
		a = Attendence.objects.all()
		roll_number = usrprof.uid
		true_count = 0
		false_count = 0
		for x in a:
			if x.student.roll_number == roll_number:
				if x.h1 == True:
					true_count += 1
				if x.h2 == True:
					true_count += 1
				if x.h3 == True:
					true_count += 1
				if x.h4 == True:
					true_count += 1
				if x.h5 == True:
					true_count += 1
				if x.h1 == False:
					false_count += 1
				if x.h2 == False:
					false_count += 1
				if x.h3 == False:
					false_count += 1
				if x.h4 == False:
					false_count += 1
				if x.h5 == False:
					false_count += 1
		percent = (true_count/(true_count + false_count))*100
		return render(request, 'dashboard/index-student.html', {'notifications':notification,'percentage':percent, 'student_notifications': notificationstu, 'nocount': notification_count, 'student': student_now})

#ACADEMIC START
@login_required
def academic_year(request):
	usrprof = UserProfile.objects.get(user=request.user)
	if usrprof.is_admin == True:
		years = AcademicYear.objects.all()
		print(years)
		return render(request, 'dashboard/academic/academic_year.html', {'acyears':years})

@login_required
def academic_new(request):
	if request.method == 'POST':
		acyr = request.POST['name']
		a = AcademicYear()
		a.year=acyr
		a.save()
		print(a)
	usrprof = UserProfile.objects.get(user=request.user)
	if usrprof.is_admin == True:
		return render(request, 'dashboard/academic/academic_new.html')
#ACADEMIC END

#COURSE START
@login_required
def course_list(request):
	usrprof = UserProfile.objects.get(user=request.user)
	if usrprof.is_admin == True:
		crs = Course.objects.all()
		return render(request, 'dashboard/course/course_list.html', {'courses':crs})

@login_required
def course_new(request):
	usrprof = UserProfile.objects.get(user=request.user)
	if request.method == 'POST':
		crs = request.POST['name']
		a = Course()
		a.name=crs
		a.save()
		print(a.name)
		crs = Course.objects.all()
		usrprof = UserProfile.objects.get(user=request.user)
		return render(request, 'dashboard/course/course_list.html', {'courses':crs})
	else:
		return render(request, 'dashboard/course/course_new.html')
#COURSE END

#SUJECT START
@login_required
def subject_list(request):
	usrprof = UserProfile.objects.get(user=request.user)
	if usrprof.is_admin == True:
		sub = Subject.objects.all()
		return render(request, 'dashboard/subject/subject_list.html', {'subjects':sub})

@login_required
def subject_new(request):
	usrprof = UserProfile.objects.get(user=request.user)
	if request.method == 'POST':
		sub = request.POST['name']
		crs = request.POST['course']
		a = Subject()
		a.name=sub
		a.course = Course.objects.get(name=crs)
		a.save()
		print(a)
		subject = Subject.objects.all()
		return render(request, 'dashboard/subject/subject_list.html', {'subjects':subject})
	if usrprof.is_admin == True:
		crs = Course.objects.all()
		print(crs)
		return render(request, 'dashboard/subject/subject_new.html', {'courses':crs})
#SUBJECT END

#SEMESTER START
@login_required
def semester_list(request):
	usrprof = UserProfile.objects.get(user=request.user)
	if usrprof.is_admin == True:
		sem = Semester.objects.all()
		print(sem)
		return render(request, 'dashboard/semester/semester_list.html', {'semesters':sem})

@login_required
def semester_new(request):
	if request.method == 'POST':
		sem = request.POST['number']
		crs = request.POST['course']
		a = Semester()
		a.number=sem
		a.course = Course.objects.get(name=crs)
		a.save()
		print(a)
	usrprof = UserProfile.objects.get(user=request.user)
	if usrprof.is_admin == True:
		crs = Course.objects.all()
		print(crs)
		return render(request, 'dashboard/semester/semester_new.html', {'courses':crs})
#SEMESTER END



#ATTENDENCE SELECT
@login_required
def attendence_select(request):
	z = AttendenceFlag.objects.get(id=1)
	print(date.today())
	if z.fdate != date.today():
		stux = Student.objects.all()
		for x in stux:
			b = Attendence()
			b.student = x
			b.date = date.today()
			b.h1 = 'False'
			b.h2 = 'False'
			b.h3 = 'False'
			b.h4 = 'False'
			b.h5 = 'False'
			b.save()
			z.fdate = date.today()
			z.save()
	if request.method == 'POST':
		tacyr = request.POST['ac_year']
		tcrs = request.POST['course']
		tsem = request.POST['semester']
		acyr = AcademicYear.objects.get(year = tacyr)
		crs_list = Course.objects.get(name = tcrs)
		sem_list = Semester.objects.get(number = tsem)
		student = Student.objects.filter(academic_year = acyr, course = crs_list, semester = sem_list)
		hour = Hours.objects.all()
		attendence = Attendence.objects.filter(date = date.today())
		return render(request, 'dashboard/attendence/attendence_mark.html', {'students':student, 'hours':hour, 'attendences':attendence, 'xcrs':tcrs, 'xsem':sem_list})
	usrprof = UserProfile.objects.get(user=request.user)
	if usrprof.is_admin == True or usrprof.is_teacher == True:
		course = Course.objects.all()
		semester = Semester.objects.all()
		year = AcademicYear.objects.all()
		admin = AdminProfile.objects.get(id=1)
		students_count = Student.objects.all().count()
		notification = Notification.objects.all()
		todays = date.today
		if usrprof.is_teacher == True:
			admin = UserProfile.objects.get(user=request.user)
		return render(request, 'dashboard/attendence/attendence_select.html', {'courses':course, 'semesters':semester, 'years':year, 'admins':admin, 'students_counts':students_count, 'notifications':notification, 'today':todays})

@login_required
def attendence_mark(request):
	usrprof = UserProfile.objects.get(user=request.user)
	if request.method == 'POST':
		rlno = request.POST['roll_number']
		idx = request.POST['id']
		a = Attendence.objects.get(id = idx)
		a.student = Student.objects.get(roll_number=rlno)
		a.h1 = request.POST['hour1']
		a.h2 = request.POST['hour2']
		a.h3 = request.POST['hour3']
		a.h4 = request.POST['hour4']
		a.h5 = request.POST['hour5']
		a.save()
		course = Course.objects.all()
		semester = Semester.objects.all()
		year = AcademicYear.objects.all()
		admin = AdminProfile.objects.get(id=1)
		if usrprof.is_teacher == True:
			admin = UserProfile.objects.get(user=request.user)
		return render(request, 'dashboard/attendence/attendence_select.html', {'courses':course, 'semesters':semester, 'years':year, 'admins':admin})
	else:
		return HttpResponseRedirect('attendence_mark')


@login_required
def student_select(request):
		student = Student.objects.all()
		return render(request, 'dashboard/profile/student_select.html',{'students':student})

@login_required
def student_profile_roll(request, pk):
		student = Student.objects.get(roll_number = pk)
		print(student)
		return render(request, 'dashboard/profile/student_profile.html', {'student':student})

@login_required
def student_profile_edit(request, pk):
	if request.method == 'POST':
		a = Student.objects.get(roll_number = pk)
		a.name = request.POST['name']
		x = request.FILES['image']
		a.image = x
		a.roll_number = request.POST['roll_number']
		a.phone_number = request.POST['phone_number']
		a.email_id = request.POST['email_id']
		a.address = request.POST['address']
		a.save()
		print(a)
		student = Student.objects.get(roll_number = pk)
		return render(request, 'dashboard/profile/student_profile.html', {'student':student})
	else:
		student = Student.objects.get(roll_number = pk)
		print(student)
		return render(request, 'dashboard/profile/student_profile_edit.html', {'student':student})

@login_required
def student_profile_add(request):
	if request.method == 'POST':
		a = Student()
		a.name = request.POST['name']
		a.image = request.FILES['img']
		a.academic_year = AcademicYear.objects.get(year = request.POST['academic_year'])
		a.course = Course.objects.get(name = request.POST['course'])
		a.semester = Semester.objects.get(number = request.POST['semester'])
		a.roll_number = request.POST['roll_number']
		a.admission_number = request.POST['admission_number']
		a.registration_number = request.POST['registration_number']
		a.phone_number = request.POST['phone_number']
		a.email_id = request.POST['email_id']
		a.address = request.POST['address']
		a.save()
		user = User.objects.create_user(username = a.roll_number, password = a.roll_number)
		x = UserProfile()
		x.user = User.objects.get(username = a.roll_number)
		x.is_student = 'True'
		x.uid = a.roll_number
		x.save()
		#user.username = a.roll_number
		#user.password = a.roll_number
		#user.save()
		auth.authenticate(username = a.roll_number, password = a.roll_number)
		return render(request, 'dashboard/profile/student_select.html')
	else:
		acyrs = AcademicYear.objects.all()
		crs = Course.objects.all()
		sem = Semester.objects.all()
		return render(request, 'dashboard/profile/student_profile_add.html', {'academic_years':acyrs, 'courses':crs, 'semesters':sem})

@login_required
def student_profile(request):
	if request.method =='POST':
		student = Student.objects.get(roll_number = request.POST['name'])
		print(student)
		return render(request, 'dashboard/profile/student_profile.html', {'student':student})

@login_required
def my_profile(request):
	if request.method =='POST':
		return render(request, 'dashboard/profile/student_profile.html')

@login_required
def notification_view(request):
	x = Notification.objects.all()	
	return render(request, 'dashboard/notification/college_view.html', {'notifications':x})

@login_required
def notification_edit(request, pk):
	if request.method == 'POST':
		a = Notification.objects.get(id=pk)
		a.content = request.POST['content']
		a.date = date.today()
		edate = request.POST['end_date']
		print(date.today)
		a.end_date = datetime.strptime(edate, '%Y-%M-%d').strftime('%Y-%M-%d')
		a.save()
		print(a)
		x = Notification.objects.all()
		return render(request, 'dashboard/notification/college_view.html', {'notifications':x})
	else:
		a = Notification.objects.get(id = pk)
		return render(request, 'dashboard/notification/college_edit.html', {'notifications':a})

@login_required
def notification_add(request):
	if request.method == 'POST':
		a = Notification()
		a.content = request.POST['content']
		a.date = date.today()
		edate = request.POST['end_date']
		a.end_date = datetime.strptime(edate, '%Y-%M-%d').strftime('%Y-%M-%d')
		a.save()
		x = Notification.objects.all()
		return render(request, 'dashboard/notification/college_view.html', {'notifications':x})
	else:
		return render(request, 'dashboard/notification/college_add.html')



@login_required
def notification_student_view(request):
	usrprof = UserProfile.objects.get(user=request.user)
	x = NotificationStudent.objects.all()
	y = Course.objects.all()
	admin = UserProfile.objects.get(user=request.user)
	if usrprof.is_teacher == True:
		admin = UserProfile.objects.get(user=request.user)
	return render(request, 'dashboard/notification/student_view.html', {'notifications':x, 'courses':y, 'admins':admin})

@login_required
def notification_student_edit(request, pk):
	if request.method == 'POST':
		a = NotificationStudent.objects.get(id=pk)
		a.content = request.POST['content']
		a.course = Course.objects.get(name =request.POST['course'])
		print(a.course)
		a.date = date.today()
		edate = request.POST['end_date']
		a.end_date = datetime.strptime(edate, '%Y-%M-%d').strftime('%Y-%M-%d')
		a.save()
		print(a)
		x = NotificationStudent.objects.all()
		y = Course.objects.all()
		return render(request, 'dashboard/notification/student_view.html', {'notifications':x, 'courses':y})
	else:
		a = NotificationStudent.objects.get(id = pk)
		y = Course.objects.all()
		return render(request, 'dashboard/notification/student_edit.html', {'notifications':a, 'courses':y})

@login_required
def notification_student_add(request):
	if request.method == 'POST':
		a = NotificationStudent()
		a.content = request.POST['content']
		a.course = Course.objects.get(name =request.POST['course'])
		a.date = date.today()
		edate = request.POST['end_date']
		a.end_date = datetime.strptime(edate, '%Y-%M-%d').strftime('%Y-%M-%d')
		a.save()
		print(a)
		x = NotificationStudent.objects.all()
		y = Course.objects.all()
		return render(request, 'dashboard/notification/student_view.html', {'notifications':x})
	else:
		y = Course.objects.all()
		return render(request, 'dashboard/notification/student_add.html', {'courses':y})

@login_required

def seminar_add(request):
	if request.method == 'POST':
		a = SeminarAssignmentProject()
		usrprof = UserProfile.objects.get(user=request.user)
		a.student = Student.objects.get(roll_number = usrprof.uid)
		a.typ = 'seminar'
		a.submited_to = Teacher.objects.get(teacher_id = request.POST['teacher'])
		a.title = request.POST['title']
		a.abstract = request.POST['abstract']
		a.file = request.FILES['file']
		a.date = date.today()
		a.save()
		teacher = Teacher.objects.all()
		notification = Notification.objects.all()
		notificationstu = NotificationStudent.objects.all()
		notification_count = NotificationStudent.objects.all().count()
		student_now = Student.objects.get(roll_number = usrprof.uid)
		return render(request, 'dashboard/index-student.html', {'notifications':notification, 'student_notifications':	notificationstu, 'nocount': notification_count, 'student': student_now})
	else:
		teacher = Teacher.objects.all()
		usrprof = UserProfile.objects.get(user=request.user)
		notification = Notification.objects.all()
		notificationstu = NotificationStudent.objects.all()
		notification_count = NotificationStudent.objects.all().count()
		student_now = Student.objects.get(roll_number = usrprof.uid)
		true_count =0
		false_count = 0
		a = Attendence.objects.all()
		roll_number = usrprof.uid
		for x in a:
			if x.student.roll_number == roll_number:
				if x.h1 == True:
					true_count += 1
				if x.h2 == True:
					true_count += 1
				if x.h3 == True:
					true_count += 1
				if x.h4 == True:
					true_count += 1
				if x.h5 == True:
					true_count += 1
				if x.h1 == False:
					false_count += 1
				if x.h2 == False:
					false_count += 1
				if x.h3 == False:
					false_count += 1
				if x.h4 == False:
					false_count += 1
				if x.h5 == False:
					false_count += 1
		percent = (true_count/(true_count + false_count))*100

		return render(request, 'dashboard/seminar/add.html', {'teachers':teacher, 'notifications':notification, 'percentage':percent, 'student_notifications': notificationstu, 'nocount': notification_count, 'student': student_now})

@login_required
def project_add(request):
	if request.method == 'POST':
		usrprof = UserProfile.objects.get(user=request.user)
		a.student = Student.objects.get(roll_number = usrprof.uid)
		a = SeminarAssignmentProject()
		a.typ = 'project'
		a.title = request.POST['title']
		a.abstract = request.POST['abstract']
		a.file = request.FILES['file']
		a.date = date.today()
		a.save()
		teacher = Teacher.objects.all()
		notification = Notification.objects.all()
		notificationstu = NotificationStudent.objects.all()
		notification_count = NotificationStudent.objects.all().count()
		student_now = Student.objects.get(roll_number = usrprof.uid)
		return render(request, 'dashboard/index-student.html', {'notifications':notification, 'student_notifications': notificationstu, 'nocount': notification_count, 'student': student_now})
	else:
		teacher = Teacher.objects.all()
		usrprof = UserProfile.objects.get(user=request.user)
		notification = Notification.objects.all()
		notificationstu = NotificationStudent.objects.all()
		notification_count = NotificationStudent.objects.all().count()
		student_now = Student.objects.get(roll_number = usrprof.uid)
		a = Attendence.objects.all()
		roll_number = usrprof.uid
		true_count = 0
		false_count = 0
		for x in a:
			if x.student.roll_number == roll_number:
				if x.h1 == True:
					true_count += 1
				if x.h2 == True:
					true_count += 1
				if x.h3 == True:
					true_count += 1
				if x.h4 == True:
					true_count += 1
				if x.h5 == True:
					true_count += 1
				if x.h1 == False:
					false_count += 1
				if x.h2 == False:
					false_count += 1
				if x.h3 == False:
					false_count += 1
				if x.h4 == False:
					false_count += 1
				if x.h5 == False:
					false_count += 1
		percent = (true_count/(true_count + false_count))*100
		return render(request, 'dashboard/project/add.html', {'teachers':teacher, 'notifications':notification,'percentage':percent, 'student_notifications': notificationstu, 'nocount': notification_count, 'student': student_now})


@login_required
def assignment_add(request):
	if request.method == 'POST':
		a = SeminarAssignmentProject()
		a.typ = 'assignment'
		a.title = request.POST['title']
		a.abstract = request.POST['abstract']
		a.file = request.FILES['file']
		a.date = date.today()
		a.save()
		teacher = Teacher.objects.all()
		notification = Notification.objects.all()
		notificationstu = NotificationStudent.objects.all()
		notification_count = NotificationStudent.objects.all().count()
		student_now = Student.objects.get(roll_number = usrprof.uid)
		return render(request, 'dashboard/index-student.html', {'notifications':notification, 'student_notifications': notificationstu, 'nocount': notification_count, 'student': student_now})
	else:
		teacher = Teacher.objects.all()
		usrprof = UserProfile.objects.get(user=request.user)
		notification = Notification.objects.all()
		notificationstu = NotificationStudent.objects.all()
		notification_count = NotificationStudent.objects.all().count()
		student_now = Student.objects.get(roll_number = usrprof.uid)
		a = Attendence.objects.all()
		roll_number = usrprof.uid
		true_count = 0
		false_count = 0
		for x in a:
			if x.student.roll_number == roll_number:
				if x.h1 == True:
					true_count += 1
				if x.h2 == True:
					true_count += 1
				if x.h3 == True:
					true_count += 1
				if x.h4 == True:
					true_count += 1
				if x.h5 == True:
					true_count += 1
				if x.h1 == False:
					false_count += 1
				if x.h2 == False:
					false_count += 1
				if x.h3 == False:
					false_count += 1
				if x.h4 == False:
					false_count += 1
				if x.h5 == False:
					false_count += 1
		percent = (true_count/(true_count + false_count))*100
		return render(request, 'dashboard/assignment/add.html', {'teachers':teacher, 'notifications':notification,'percentage':percent, 'student_notifications': notificationstu, 'nocount': notification_count, 'student': student_now})






#@login_required
#def student_profile_edit(request, pk):
#	if request.method == 'POST':
#		a = Student.objects.get(roll_number = pk)
#		a.name = request.POST['name']
#		x = request.FILES['image']
#		a.image = x
#		a.roll_number = request.POST['roll_number']
#		a.phone_number = request.POST['phone_number']
#		a.email_id = request.POST['email_id']
#		a.address = request.POST['address']
#		a.save()
#		print(a)
#		student = Student.objects.get(roll_number = pk)
#		return render(request, 'dashboard/profile/student_profile.html', {'student':student})
#	else:
#		student = Student.objects.get(roll_number = pk)
#		print(student)
#		return render(request, 'dashboard/profile/student_profile_edit.html', {'student':student})

@login_required
def teacher_profile_add(request):
	if request.method == 'POST':
		a = Teacher()
		a.image = request.FILES['img']
		a.name = request.POST['name']
		a.teacher_id = name = request.POST['teacherid']
		a.email_id = number = request.POST['emailid']
		a.address = request.POST['address']
		a.department = Department.objects.get(name = request.POST['dept'])
		a.save()
		user = User.objects.create_user(username = a.teacher_id, password = a.teacher_id)
		x = UserProfile()
		x.user = User.objects.get(username = a.teacher_id)
		x.is_teacher = 'True'
		x.uid = a.teacher_id
		x.save()
		#user.username = a.roll_number
		#user.password = a.roll_number
		#user.save()
		auth.authenticate(username = a.teacher_id, password = a.teacher_id)
		return render(request, 'dashboard/profile/teacher_profile_add.html')
	else:
		dept = Department.objects.all()
		return render(request, 'dashboard/profile/teacher_profile_add.html', {'departments':dept})

#@login_required
#def student_profile(request):
#	if request.method =='POST':
#		student = Student.objects.get(name = request.POST['name'])
#		print(student)
#		return render(request, 'dashboard/profile/student_profile.html', {'student':student})


@login_required
def attendence_view(request):	
	usrprof = UserProfile.objects.get(user=request.user)
	roll_number = usrprof.uid
	a = Attendence.objects.all()
	print(roll_number)
	notification = Notification.objects.all()
	notificationstu = NotificationStudent.objects.all()
	notification_count = NotificationStudent.objects.all().count()
	student_now = Student.objects.get(roll_number = usrprof.uid)
	true_count =0
	false_count = 0
	for x in a:
		if x.student.roll_number == roll_number:
			if x.h1 == True:
				true_count += 1
			if x.h2 == True:
				true_count += 1
			if x.h3 == True:
				true_count += 1
			if x.h4 == True:
				true_count += 1
			if x.h5 == True:
				true_count += 1
			if x.h1 == False:
				false_count += 1
			if x.h2 == False:
				false_count += 1
			if x.h3 == False:
				false_count += 1
			if x.h4 == False:
				false_count += 1
			if x.h5 == False:
				false_count += 1
	percent = (true_count/(true_count + false_count))*100

	return render(request, 'dashboard/attendence/attendence_view.html', {'attendences':a, 'roll_number':roll_number, 'notifications':notification, 'student_notifications': notificationstu,'percentage':percent, 'nocount': notification_count, 'student': student_now})
	
	
@login_required
def view_uploads(request):
	a = SeminarAssignmentProject.objects.all()
	return render(request, 'dashboard/view_uploads.html', {'uploads':a})