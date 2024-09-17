# Generated by Django 5.1.1 on 2024-09-16 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ReportCardApp", "0002_subject_subjectmarks"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rank",
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
                ("date_of_report_card_generation", models.DateField(auto_created=True)),
                ("student_rank", models.IntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="studentrank",
                        to="ReportCardApp.student",
                    ),
                ),
            ],
        ),
    ]