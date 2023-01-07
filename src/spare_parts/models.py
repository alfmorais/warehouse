from django.db import models


class SpareParts(models.Model):
    description = models.CharField(
        verbose_name="Nome da Peça",
        max_length=255,
        null=False,
        blank=False,
    )
    number = models.CharField(
        verbose_name="Número de Identificação da Peça",
        max_length=255,
        null=False,
        blank=False,
    )
    minimum_stock = models.PositiveIntegerField(
        verbose_name="Quantidade Miníma de Estoque",
        null=True,
        blank=True,
    )
    maximum_stock = models.PositiveIntegerField(
        verbose_name="Quantidade Maxíma de Estoque",
        null=True,
        blank=True,
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Quantidade Atual do Estoque",
        null=True,
        blank=True,
    )
    TYPE = (
        ("feedstock", "Matéria-prima"),
        ("retail-goods", "Bens para varejo"),
        ("internal-consumption", "Consumo interno da organização"),
        ("safety-stock", "Estoque de segurança"),
    )
    type = models.CharField(
        verbose_name="Tipo do Material",
        max_length=32,
        choices=TYPE,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.id}, {self.description}, {self.number}"

    class Meta:
        verbose_name = "Peça"
        verbose_name_plural = "Peças"
