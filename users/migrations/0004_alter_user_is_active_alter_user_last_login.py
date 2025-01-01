# Generated by Django 5.1.3 on 2025-01-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_payment_link_payment_session_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="Статус активности"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Дата последнего входа"
            ),
        ),
    ]
