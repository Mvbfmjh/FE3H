# Generated by Django 4.1.6 on 2023-02-09 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FE3HApp', '0002_character_aristocrat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubjectLevel',
        ),
        migrations.AlterField(
            model_name='battalion',
            name='auth_requirement',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_armor',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_authority',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_axe',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_bow',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_brawl',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_faith',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_flying',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_lance',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_reason',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_riding',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='currentunit',
            name='prof_sword',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_armor',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_authority',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_axe',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_bow',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_brawl',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_faith',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_flying',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_lance',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_reason',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_riding',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='unitclass',
            name='prof_sword',
            field=models.CharField(choices=[('E', 'E'), ('E+', 'E+'), ('D', 'D'), ('D+', 'D+'), ('C', 'C'), ('C+', 'C+'), ('B', 'B'), ('B+', 'B+'), ('A', 'A'), ('A+', 'A+'), ('S', 'S'), ('S+', 'S+')], default='', max_length=2, null=True),
        ),
    ]