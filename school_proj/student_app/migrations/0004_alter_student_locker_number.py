# Generated by Django 4.2.7 on 2023-11-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_alter_student_good_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_number',
            field=models.IntegerField(default=110, unique=True),
        ),
    ]
