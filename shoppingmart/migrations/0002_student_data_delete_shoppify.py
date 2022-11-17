# Generated by Django 4.1.3 on 2022-11-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingmart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Area', models.CharField(max_length=50)),
                ('About_user', models.TextField()),
                ('Birthday', models.DateField()),
                ('prof_pic', models.ImageField(default='', max_length=50, upload_to='profile_pics')),
            ],
        ),
        migrations.DeleteModel(
            name='shoppify',
        ),
    ]
