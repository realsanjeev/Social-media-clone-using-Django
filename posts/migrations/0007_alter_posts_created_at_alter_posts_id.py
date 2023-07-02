# Generated by Django 4.2.2 on 2023-07-02 14:49

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_posts_created_at_alter_posts_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 2, 20, 34, 49, 8151)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.UUIDField(default=uuid.UUID('db1633ed-c153-4fa3-b56d-26b154e20092'), primary_key=True, serialize=False),
        ),
    ]