# Generated by Django 4.1.3 on 2022-12-19 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0002_alter_member_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
    ]
