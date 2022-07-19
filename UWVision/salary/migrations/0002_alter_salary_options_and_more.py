# Generated by Django 4.0.5 on 2022-07-16 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salary',
            options={'verbose_name_plural': 'Salaries'},
        ),
        migrations.AlterField(
            model_name='salary',
            name='monthly_misc_stipends',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='monthly_relocation_stipend',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='term_signing_bonus',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
