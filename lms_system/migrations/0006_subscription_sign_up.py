# Generated by Django 5.1.3 on 2025-01-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms_system", "0005_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="sign_up",
            field=models.BooleanField(default=False, verbose_name="Подписка"),
        ),
    ]
