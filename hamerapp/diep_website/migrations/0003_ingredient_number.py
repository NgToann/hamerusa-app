# Generated by Django 4.0 on 2022-02-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diep_website', '0002_alter_slide_options_slide_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Thứ tự'),
        ),
    ]