# Generated by Django 2.1 on 2019-03-01 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_attendence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationstudent',
            name='semester',
        ),
    ]
