# Generated by Django 4.1.3 on 2022-12-19 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dex.company'),
        ),
    ]