# Generated by Django 3.2.3 on 2021-06-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readCsv', '0002_auto_20210623_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='SC_No_Boys_Appeared',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='SC_No_Boys_Passed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='SC_No_Girls_Appeared',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='SC_No_Girls_Passed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='SC_No_Total_Appeared',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='SC_No_Total_Passed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='ST_No_Boys_Appeared',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='ST_No_Boys_Passed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='ST_No_Girls_Appeared',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='ST_No_Girls_Passed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='ST_No_Total_Appeared',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='ST_No_Total_Passed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='current_timeStamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
