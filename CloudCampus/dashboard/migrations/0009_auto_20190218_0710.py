# Generated by Django 2.1 on 2019-02-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='course',
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='zskolr/static/UserDP/default.png', upload_to='zskolr/static/UserDP/'),
        ),
    ]
