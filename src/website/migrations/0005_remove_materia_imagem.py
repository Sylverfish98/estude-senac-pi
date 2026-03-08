from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0004_topic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="materia",
            name="imagem",
        ),
    ]
