# Generated by Django 3.2.2 on 2021-08-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_rename_type_assignment_assignment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='picture',
            field=models.ImageField(default='', upload_to='lms/image'),
        ),
    ]
