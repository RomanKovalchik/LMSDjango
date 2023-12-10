# Generated by Django 4.2.7 on 2023-12-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(null=True)),
                ('lesson', models.TextField(null=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
