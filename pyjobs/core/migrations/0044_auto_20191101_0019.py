# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-01 00:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20191029_1916'),
    ]

    database_operations = [
        migrations.AlterModelTable('MailingList', 'marketing_mailinglist'),
        migrations.AlterModelTable('Contact', 'marketing_contact')
    ]

    state_operations = [
        migrations.DeleteModel('MailingList'),
        migrations.DeleteModel('Contact')
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations
        )
    ]
