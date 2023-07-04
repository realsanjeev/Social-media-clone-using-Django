# Generated by Django 4.2.2 on 2023-07-04 04:15

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_posts_created_at_alter_posts_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 4, 10, 0, 27, 124000)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cb1e6a3b-99e3-4e8e-bb47-533c29163607'), primary_key=True, serialize=False),
        ),
    ]
