# Generated by Django 3.2.9 on 2021-12-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_students_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.ImageField(upload_to='students/%Y/%m/%d/', verbose_name='image'),
        ),
    ]
