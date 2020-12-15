# Generated by Django 3.0.7 on 2020-10-12 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0044_merge_20201011_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='occupied',
            new_name='occupied_MRSB',
        ),
        migrations.AddField(
            model_name='applicant',
            name='occupied_Tulsi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicant',
            name='occupied_Type1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='date_applied',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]