# Generated by Django 3.0.5 on 2020-05-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankiety', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('question_text', models.CharField(max_length=200)),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
    ]