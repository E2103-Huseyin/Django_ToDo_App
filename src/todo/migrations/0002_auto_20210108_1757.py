# Generated by Django 3.1.5 on 2021-01-08 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('-create_date',)},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='complated',
            new_name='completed',
        ),
    ]
