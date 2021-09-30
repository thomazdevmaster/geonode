# Generated by Django 2.2.20 on 2021-09-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_commands_http', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managementcommandjob',
            name='args',
            field=models.TextField(blank=True, default='[]', help_text='JSON encoded positional arguments (Example: ["arg1", "arg2"])', verbose_name='Positional Arguments'),
        ),
        migrations.AlterField(
            model_name='managementcommandjob',
            name='kwargs',
            field=models.TextField(blank=True, default='{}', help_text='JSON encoded keyword arguments (Example: {"argument": "value"})', verbose_name='Keyword Arguments'),
        ),
    ]
