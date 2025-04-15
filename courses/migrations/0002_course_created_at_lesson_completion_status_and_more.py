# Generated by Django 5.1.4 on 2025-04-08 11:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='completion_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lesson',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='completed_lessons',
            field=models.ManyToManyField(blank=True, related_name='completed_by', to='courses.lesson'),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(help_text='Duration in hours'),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='courses_thumbnail/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrolled_courses',
            field=models.ManyToManyField(related_name='students', to='courses.course'),
        ),
    ]
