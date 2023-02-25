# Generated by Django 4.1.7 on 2023-02-23 20:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_organization_organizationuser_organization_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrganizationInvitation",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("mainapp.organizationuser",),
        ),
        migrations.AlterUniqueTogether(
            name="organizationuser",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="organizationuser",
            name="invitation_key",
            field=models.UUIDField(editable=False, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="organizationuser",
            name="invitee_email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="organizationuser",
            name="inviter",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="inviter",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="organizationuser",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="organizationuser",
            unique_together={("user", "organization", "invitee_email")},
        ),
    ]
