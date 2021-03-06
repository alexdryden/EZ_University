# Generated by Django 2.1.5 on 2019-03-23 22:52

from django.db import migrations, models

start_year = 2018
duration = 3

YEARS = [
    {'year': str(start_year+i)} for i in range(duration)
]
YEARS.append({'year':'9999'})
def add_year_data(apps, schema_editor):
    year_model_class = apps.get_model('courseinfo', 'Year')
    for year in YEARS:
        year_object = year_model_class.objects.create(
            year=year['year'],
        )

def remove_year_data(apps, schema_editor):
    year_model_class = apps.get_model('courseinfo', 'Year')
    for year in YEARS:
        year_object = year_model_class.objects.get(
            year=year['year'],
        )
        year_object.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0006_period_schema_and_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['year'],
            },
        ),
        migrations.AlterField(
            model_name='period',
            name='period_name',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.RunPython(
            add_year_data,
            remove_year_data
        )

    ]
