# Generated by Django 2.1 on 2019-02-26 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20190226_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='student',
        ),
        migrations.DeleteModel(
            name='Attendence',
        ),
    ]
