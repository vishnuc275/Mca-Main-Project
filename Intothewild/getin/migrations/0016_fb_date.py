# Generated by Django 3.0.5 on 2022-06-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getin', '0015_staffreg_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fb',
            name='date',
            field=models.CharField(blank=True, default='{% now "d/m/Y" %}', max_length=100, null=True),
        ),
    ]
