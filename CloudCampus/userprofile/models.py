from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_teacher = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)
	is_hod = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_parent = models.BooleanField(default=False)
	uid = models.IntegerField()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
