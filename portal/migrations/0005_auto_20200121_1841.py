# Generated by Django 3.0.2 on 2020-01-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0004_auto_20200121_1838"),
    ]

    operations = [
        migrations.AlterField(
            model_name="queuer",
            name="proof_document",
            field=models.FileField(upload_to="user_directory_path"),
        ),
        migrations.AlterField(
            model_name="queuer",
            name="wife_name",
            field=models.CharField(max_length=126),
        ),
    ]