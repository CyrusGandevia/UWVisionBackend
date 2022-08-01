# Generated by Django 4.0.5 on 2022-08-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_question', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewquestion',
            name='coop_term_number',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True),
        ),
        migrations.AlterField(
            model_name='interviewquestion',
            name='program',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='interviewquestion',
            name='term_worked',
            field=models.CharField(blank=True, choices=[('Fall', 'Fall'), ('Spring', 'Spring'), ('Winter', 'Winter')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='interviewquestion',
            name='year_worked',
            field=models.IntegerField(blank=True, choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, null=True),
        ),
    ]
