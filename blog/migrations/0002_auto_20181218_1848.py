# Generated by Django 2.1.4 on 2018-12-19 02:48

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False 
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Blogger',
        ),
    ]
