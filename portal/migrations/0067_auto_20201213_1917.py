# Generated by Django 3.0.7 on 2020-12-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0066_auto_20201213_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='application_received_by_hcu_date',
            field=models.DateTimeField(verbose_name='Application Received by H.C.Unit Date:'),
        ),
    ]
