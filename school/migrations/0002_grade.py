# Generated by Django 4.1.2 on 2022-10-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_5th', models.IntegerField()),
                ('grade_6th', models.IntegerField()),
                ('grade_10th', models.IntegerField()),
            ],
        ),
    ]
