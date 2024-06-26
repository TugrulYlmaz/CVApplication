# Generated by Django 5.0.4 on 2024-05-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0009_experience_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='job_location',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='job_title',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='start_date',
        ),
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='experience',
            name='parameter',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Parameter'),
        ),
    ]
