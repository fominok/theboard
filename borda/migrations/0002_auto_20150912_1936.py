# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='msg',
            new_name='post_text',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='name',
            new_name='thread_text',
        ),
    ]
