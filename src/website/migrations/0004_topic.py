import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0003_subjects_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
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
                ("nome", models.CharField(max_length=120)),
                ("link", models.URLField(blank=True, null=True)),
                ("is_completed", models.BooleanField(default=False)),
                ("data_estudo", models.DateField(blank=True, null=True)),
                ("index", models.PositiveIntegerField(default=0)),
                (
                    "materia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="topics",
                        to="website.materia",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tópico",
                "verbose_name_plural": "Tópicos",
                "ordering": ["data_estudo", "index", "id"],
            },
        ),
        migrations.AddIndex(
            model_name="topic",
            index=models.Index(fields=["data_estudo"], name="website_top_data_es_3d4606_idx"),
        ),
        migrations.AddIndex(
            model_name="topic",
            index=models.Index(
                fields=["materia", "data_estudo"],
                name="website_top_materia_0f9b33_idx",
            ),
        ),
    ]
  
