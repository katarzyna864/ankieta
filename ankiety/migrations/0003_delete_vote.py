# Generated by Django 3.0.5 on 2020-05-09 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ankiety', '0002_vote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]