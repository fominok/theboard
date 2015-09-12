# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borda', '0002_auto_20150912_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='thread_text',
            new_name='name',
        ),
    ]
