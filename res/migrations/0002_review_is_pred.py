# Generated by Django 4.0.4 on 2022-05-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_pred',
            field=models.BooleanField(default=True),
        ),
    ]
