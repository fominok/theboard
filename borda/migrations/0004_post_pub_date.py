# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('borda', '0003_auto_20150912_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date post', default=datetime.datetime(2015, 9, 14, 10, 8, 24, 496096, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
