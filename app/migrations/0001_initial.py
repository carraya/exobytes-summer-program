# Generated by Django 3.2 on 2021-06-23 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(choices=[('SS', 'Subsystems'), ('M1', 'Motion Level 1'), ('M2', 'Motion Level 2')], default='SS', max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='ZoomLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day1', models.URLField(max_length=1000)),
                ('day2', models.URLField(max_length=1000)),
                ('day3', models.URLField(max_length=1000)),
                ('day4', models.URLField(max_length=1000)),
                ('day5', models.URLField(max_length=1000)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coursetype')),
            ],
        ),
    ]