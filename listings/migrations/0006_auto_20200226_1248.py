# Generated by Django 2.2.7 on 2020-02-26 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20200225_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='wifi',
            field=models.CharField(default="Not Available", max_length=200),
            preserve_default=False,
        ),
    ]
