# Generated by Django 2.1.5 on 2019-01-13 01:31

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_mushroomspot_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='mushroomspot',
            name='geometry',
            field=djgeojson.fields.GeometryField(blank=True),
        ),
        migrations.AddField(
            model_name='mushroomspot',
            name='polygon',
            field=djgeojson.fields.PolygonField(blank=True),
        ),
        migrations.AddField(
            model_name='mushroomspot',
            name='string',
            field=djgeojson.fields.LineStringField(blank=True),
        ),
    ]
