# Generated by Django 3.0.14 on 2022-05-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('UserID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('User_Password', models.CharField(max_length=100)),
            ],
        ),
    ]
