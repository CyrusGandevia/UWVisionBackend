# Generated by Django 4.0.5 on 2022-07-19 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0003_alter_salary_year_worked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary',
            old_name='job_id',
            new_name='job',
        ),
    ]
