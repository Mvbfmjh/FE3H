# Generated by Django 4.1.6 on 2023-02-13 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FE3HApp', '0005_alter_currentunit_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentunit',
            name='battalion',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FE3HApp.battalion'),
        ),
    ]
