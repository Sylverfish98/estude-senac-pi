from django.db import models


class Topic(models.Model):
    materia = models.ForeignKey(
        "website.Materia",
        on_delete=models.CASCADE,
        related_name="topics",
    )
    nome = models.CharField(max_length=120)
    link = models.URLField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    data_estudo = models.DateField(blank=True, null=True)
    index = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["data_estudo", "index", "id"]
        verbose_name = "Tópico"
        verbose_name_plural = "Tópicos"
        indexes = [
            models.Index(fields=["data_estudo"]),
            models.Index(fields=["materia", "data_estudo"]),
        ]

    def __str__(self) -> str:
        return self.nome
