# Generated by Django 4.0.4 on 2022-05-09 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0004_alter_place_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sightseeing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sight_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=3000)),
                ('images', models.ImageField(upload_to='photos/sightseeing')),
                ('images_360_1', models.ImageField(null=True, upload_to='photos/image_360')),
                ('images_360_2', models.ImageField(null=True, upload_to='photos/image_360')),
                ('images_360_3', models.ImageField(null=True, upload_to='photos/image_360')),
                ('yaw1', models.IntegerField()),
                ('yaw2', models.IntegerField()),
                ('yaw3', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place')),
            ],
        ),
    ]
