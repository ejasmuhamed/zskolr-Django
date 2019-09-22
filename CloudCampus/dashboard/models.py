from django.db import models
from datetime import date

class AcademicYear(models.Model):
	year = models.CharField(max_length = 9)
	def __str__(self):
		return self.year

class Course(models.Model):
	name = models.CharField(max_length = 30)
	def __str__(self):
		return self.name


class Subject(models.Model):
	course = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
	name = models.CharField(max_length = 20)
	def __str__(self):
		return self.name 	

class Semester(models.Model):
	number = models.IntegerField()
	#def __str__(self):
		#return self.number

class Hours(models.Model):
	number = models.IntegerField()

class Weekday(models.Model):
	name = models.CharField(max_length = 10)
	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name	

#Here Comes the complicated part
class Student(models.Model):
	academic_year = models.ForeignKey(AcademicYear, on_delete = models.DO_NOTHING)
	course = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
	semester = models.ForeignKey(Semester, on_delete = models.DO_NOTHING)
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to = 'UserDP/', default = 'UserDP/default.png')
	admission_number = models.IntegerField(primary_key=True)
	registration_number = models.IntegerField()
	roll_number = models.IntegerField()
	phone_number = models.IntegerField()
	email_id = models.EmailField(blank=True, unique=True)
	address = models.CharField(max_length=100)
	def __str__(self):
		return self.name


class Teacher(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to = 'UserDP/', default = 'UserDP/default.png')
	teacher_id = models.IntegerField(primary_key=True)
	email_id = models.EmailField(blank=True, unique=True)
	address = models.CharField(max_length=100)
	department = models.ForeignKey(Department, on_delete = models.DO_NOTHING)
	def __str__(self):
		return self.name


class Attendence(models.Model):
	student = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
	date = models.DateField()
	h1 = models.BooleanField(default=False)
	h2 = models.BooleanField(default=False)
	h3 = models.BooleanField(default=False)
	h4 = models.BooleanField(default=False)
	h5 = models.BooleanField(default=False)

class TimeTable(models.Model):
	course = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
	weekdays = models.ForeignKey(Weekday, on_delete = models.DO_NOTHING)
	hour = models.ForeignKey(Hours, on_delete = models.DO_NOTHING)
	subject = models.ForeignKey(Subject, on_delete = models.DO_NOTHING)

class NotificationStudent(models.Model):
	content = models.CharField(max_length=300)
	course = models.ForeignKey(Course, on_delete= models.DO_NOTHING)
	date = models.DateField(default = date.today)
	end_date = models.DateField()	

class Notification(models.Model):
	content = models.CharField(max_length=300)
	date = models.DateField(default = date.today)
	end_date = models.DateField()


class AdminProfile(models.Model):
	name = models.CharField(max_length=30)
	email_id = models.EmailField()
	image = models.ImageField(upload_to = 'UserDP/', default = 'UserDP/default.png')

class SeminarAssignmentProject(models.Model):
	typ_choices = (
    ("Seminar", "Seminar"),
    ("Assignment", "Assignment"),
    ("Project", "Project"),
    )
	typ = models.CharField(max_length = 20, choices=typ_choices, default="Seminar")
	title = models.CharField(max_length = 30)
	abstract = models.CharField(max_length = 1000)
	file = models.FileField(upload_to = 'UserUploads/')
	date = models.DateField(default = date.today)
	student = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
	submited_to = models.ForeignKey(Teacher, on_delete = models.DO_NOTHING)


class AttendenceFlag(models.Model):
	fdate = models.DateField()
	