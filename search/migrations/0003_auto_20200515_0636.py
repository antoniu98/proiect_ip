# Generated by Django 3.0.6 on 2020-05-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200515_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advertisment',
            name='conditions',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
