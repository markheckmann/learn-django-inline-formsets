# Generated by Django 4.1.7 on 2023-03-15 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bedarf",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Bedarf",
                "verbose_name_plural": "Bedarfe",
            },
        ),
        migrations.CreateModel(
            name="BedarVZP",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("jahr", models.IntegerField(blank=True)),
                ("vzp", models.FloatField(blank=True)),
                (
                    "bedarf",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bedarf.bedarf"
                    ),
                ),
            ],
        ),
    ]