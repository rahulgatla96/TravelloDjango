# Generated by Django 5.1.6 on 2025-02-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
