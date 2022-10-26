# Generated by Django 4.0.2 on 2022-10-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='students'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='teachers'),
        ),
    ]