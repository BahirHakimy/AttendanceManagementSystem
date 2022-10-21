# Generated by Django 4.1.2 on 2022-10-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Classes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, unique=True)),
                ("floor", models.IntegerField()),
                ("semester", models.IntegerField()),
                ("department", models.CharField(max_length=25)),
                ("room_no", models.IntegerField()),
                ("class_start_date", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "M"), ("F", "F"), ("B", "Both")], max_length=2
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=35)),
            ],
        ),
    ]