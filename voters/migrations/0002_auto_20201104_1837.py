# Generated by Django 3.1.2 on 2020-11-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='profile_pic',
            field=models.URLField(blank=True, null=True),
        ),
    ]
