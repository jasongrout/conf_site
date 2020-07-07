# Generated by Django 3.0.7 on 2020-06-24 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0011_alter_under_represented_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='proposal',
            name='accomodation_needs',
            field=models.CharField(blank=True, default='', help_text='Examples include, but not limited to: sign language, closed captioning, assistance with recording, etc. Please indicate the specific need so we can plan in advance.', max_length=200, verbose_name='Do you have specific\u200b accessibility needs at the conference\u200b?'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='requests',
            field=models.TextField(blank=True, default='', help_text='Let us know if you have specific requests or needs — for example, restrictions on when you can participate (e.g., live panels, office hours, etc.) and if you anticipate any issues recording your content.', verbose_name='Requests'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='tutorial_format',
            field=models.TextField(blank=True, help_text='Please describe what portion of the tutorial will be spent on the video presentation, hands-on exercises and self-assessment or knowledge checks (if any). This does not have to be laid minute-by-minute but give an overall idea on how the 3 hours will be distributed.'),
        ),
    ]