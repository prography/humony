# Generated by Django 2.1.7 on 2019-07-15 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picxi', '0009_auto_20190715_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outpic',
            name='seg_id',
        ),
        migrations.RemoveField(
            model_name='segpic',
            name='in_id',
        ),
    ]
