# Generated by Django 4.0.5 on 2022-06-15 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_signup_donatefund'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='donatefund',
        ),
    ]
