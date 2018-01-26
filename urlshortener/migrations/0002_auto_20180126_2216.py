# Generated by Django 2.0 on 2018-01-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='url',
            name='shortcode',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
