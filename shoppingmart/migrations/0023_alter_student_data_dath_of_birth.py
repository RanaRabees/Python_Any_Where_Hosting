# Generated by Django 4.1.3 on 2022-11-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingmart', '0022_rename_datetime_student_data_dath_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='Dath_Of_Birth',
            field=models.CharField(default='', max_length=50),
        ),
    ]
