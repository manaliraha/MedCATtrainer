# Generated by Django 2.2.12 on 2020-06-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_auto_20200520_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectannotateentities',
            name='terminate_available',
            field=models.BooleanField(default=False, help_text='enable the option to terminate concepts.'),
        ),
    ]
