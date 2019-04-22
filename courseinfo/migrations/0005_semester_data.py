# Generated by Django 2.1.5 on 2019-03-23 19:17

from django.db import migrations

year_start = 2019
duration = 2

sem = ['Summer', 'Fall', 'Spring']

SEMESTERS = [
    {'semester_name':  '%d - %s' % (year_start + i, sem[j])} for i in range(duration) for j in range(len(sem))
]


def add_semester_data(apps, schema_editor):
    semester_model_class = apps.get_model('courseinfo', 'Semester')
    for semester in SEMESTERS:
        semester_object = semester_model_class.objects.create(
            semester_name=semester['semester_name'],
        )


def remove_semester_data(apps, schema_editor):
    semester_model_class = apps.get_model('courseinfo', 'Semester')
    for semester in SEMESTERS:
        semester_object = semester_model_class.objects.get(
            semester_name=semester['semester_name'],
        )
        semester_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0004_auto_20190323_1907'),
    ]

    operations = [
        migrations.RunPython(
            add_semester_data,
            remove_semester_data
        )
    ]
