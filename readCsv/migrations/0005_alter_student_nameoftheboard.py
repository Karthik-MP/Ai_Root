# Generated by Django 3.2.3 on 2021-06-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readCsv', '0004_alter_student_current_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nameOfTheBoard',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]