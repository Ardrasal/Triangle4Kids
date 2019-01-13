# Generated by Django 2.1.5 on 2019-01-13 00:36

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_merge_20190112_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='MushroomSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', djgeojson.fields.PointField()),
            ],
        ),
    ]