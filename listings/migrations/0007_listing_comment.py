# Generated by Django 2.2.7 on 2020-05-03 11:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_ratings', '0003_auto_20200503_1358'),
        ('listings', '0006_auto_20200226_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='comment',
            field=models.ForeignKey(blank=True,null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reviews_ratings.Comment'),
            preserve_default=False,
        ),
    ]
