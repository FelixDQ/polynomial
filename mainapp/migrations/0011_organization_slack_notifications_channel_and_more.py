# Generated by Django 4.2.5 on 2023-09-24 15:29

import django_jsonform.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0010_user_last_dashboard_visit_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="slack_notifications_channel",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="slack_notifications_credentials",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="metric",
            name="integration_config",
            field=django_jsonform.models.fields.JSONField(
                blank=True, null=True, verbose_name="Integration configuration"
            ),
        ),
    ]
