# Generated by Django 5.0.4 on 2024-05-09 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0003_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('id',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]