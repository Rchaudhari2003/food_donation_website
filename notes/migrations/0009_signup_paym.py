# Generated by Django 4.0.5 on 2022-06-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_remove_signup_paym'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='paym',
            field=models.IntegerField(blank=True, default=None, max_length=15),
        ),
    ]