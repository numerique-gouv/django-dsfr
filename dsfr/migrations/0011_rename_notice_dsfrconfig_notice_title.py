# Generated by Django 4.2.15 on 2024-08-23 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dsfr", "0010_dsfrconfig_notice_icon_class_alter_dsfrconfig_notice_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dsfrconfig",
            old_name="notice",
            new_name="notice_title",
        ),
    ]
