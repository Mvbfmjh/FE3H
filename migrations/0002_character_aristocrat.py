# Generated by Django 4.1.6 on 2023-02-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FE3HApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='aristocrat',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
