# Generated by Django 4.0 on 2022-03-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diep_website', '0006_webcontent_counterfeiting_photo_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Nội dung'),
        ),
    ]