# Generated by Django 4.2.5 on 2023-09-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll_number', models.IntegerField(default=None)),
                ('date_of_birth', models.DateField(default=None)),
                ('email', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField(default=None)),
                ('address', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]