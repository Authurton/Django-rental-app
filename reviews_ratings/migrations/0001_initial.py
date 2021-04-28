# Generated by Django 2.2.7 on 2020-02-25 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(upload_to='%Y/%m/&d')),
                ('object_id', models.PositiveIntegerField()),
                ('content', models.TextField(blank=True, max_length=250, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('average_rating', models.FloatField(default=0)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.Listing')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=20, null=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Listing')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ratings', to='reviews_ratings.Review')),
            ],
        ),
    ]
