# Generated by Django 2.0.1 on 2018-02-07 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='refrence',
            field=models.CharField(default='#', max_length=1000),
            preserve_default=False,
        ),
    ]