# Generated by Django 4.2.7 on 2023-11-18 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_lesson_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='lesson',
            table='course',
        ),
    ]
