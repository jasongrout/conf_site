# Generated by Django 2.2.4 on 2019-08-21 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_proposal_travel_stipend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='travel_stipend',
            new_name='stipend',
        ),
    ]
