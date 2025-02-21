# Generated by Django 5.1.5 on 2025-01-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user_id", models.IntegerField()),
                ("product_id", models.IntegerField()),
                ("quantity", models.IntegerField()),
            ],
            options={
                "db_table": "orders",
            },
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "db_table": "products",
            },
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "db_table": "users",
            },
        ),
    ]
