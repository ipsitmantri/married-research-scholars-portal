# Generated by Django 3.0.7 on 2020-09-19 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_auto_20200919_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='queuer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Queuer'),
        ),
    ]
