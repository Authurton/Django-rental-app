# Generated by Django 2.2.7 on 2020-02-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200225_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='last_name', max_length=200),
        ),
    ]
