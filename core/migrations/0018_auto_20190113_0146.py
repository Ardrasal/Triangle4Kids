# Generated by Django 2.1.5 on 2019-01-13 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20190113_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mushroomspot',
            name='geometry',
        ),
        migrations.RemoveField(
            model_name='mushroomspot',
            name='polygon',
        ),
        migrations.RemoveField(
            model_name='mushroomspot',
            name='string',
        ),
    ]