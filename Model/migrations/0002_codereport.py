# Generated by Django 3.2.3 on 2021-06-16 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('reporter', models.CharField(max_length=30)),
                ('notice_time', models.CharField(max_length=30)),
                ('report_time', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=300)),
                ('university', models.CharField(max_length=30)),
            ],
        ),
    ]
