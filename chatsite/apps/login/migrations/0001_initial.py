# Generated by Django 3.1.7 on 2021-03-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptchaSession',
            fields=[
                ('reg_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sentence', models.CharField(max_length=96)),
                ('index', models.IntegerField()),
                ('verified', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginSession',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('rand', models.CharField(max_length=32)),
                ('valid_resp', models.CharField(max_length=256)),
            ],
        ),
    ]
