# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borda', '0004_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
