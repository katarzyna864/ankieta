# Generated by Django 3.0.5 on 2020-05-23 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankiety', '0015_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]
