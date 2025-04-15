# Generated by Django 5.1.4 on 2025-04-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_created_at_lesson_completion_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrolled_courses',
            field=models.ManyToManyField(related_name='student', to='courses.course'),
        ),
    ]
