# Generated by Django 5.0.4 on 2024-05-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0008_alter_experience_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='name',
            field=models.CharField(blank=True, default='', help_text='This is variable of the setting.', max_length=254, verbose_name='Name'),
        ),
    ]
