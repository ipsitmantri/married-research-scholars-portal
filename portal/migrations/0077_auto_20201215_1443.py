# Generated by Django 3.0.7 on 2020-12-15 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0076_auto_20201214_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='application_received_by_hcu_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Application Received by H.C.Unit Date:'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='scholarship_awarded_upto',
            field=models.DateField(blank=True, null=True, verbose_name='Initially the scholarship awarded up to'),
        ),
    ]