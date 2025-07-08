from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"

class Measurement(models.Model):
    id_sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name="measurements",
        verbose_name="Датчик"
    )
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время измерения")

    def __str__(self):
        return f"{self.id_sensor.name} - {self.temperature}°C ({self.created_at})"

    class Meta:
        verbose_name = "Измерение температуры"
        verbose_name_plural = "Измерения температуры"