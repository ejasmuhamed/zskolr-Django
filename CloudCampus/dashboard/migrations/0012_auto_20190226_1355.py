# Generated by Django 2.1 on 2019-02-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20190226_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
