# Generated by Django 4.1.4 on 2023-02-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfile', '0005_alter_student_file_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='file_student',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student_model',
            name='file_student',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
