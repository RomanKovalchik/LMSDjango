# Generated by Django 4.2.7 on 2023-11-18 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.AlterModelTable(
            name='course',
            table=None,
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('text', models.TextField(null=True)),
                ('activity', models.TextField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
            options={
                'db_table': 'course',
                'ordering': ['id'],
            },
        ),
    ]
