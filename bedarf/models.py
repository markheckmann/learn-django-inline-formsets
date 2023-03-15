from django.db import models


class Bedarf(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Bedarf"
        verbose_name_plural = "Bedarfe"

    def __str__(self):
        return self.name


class BedarfVZP(models.Model):
    bedarf = models.ForeignKey(Bedarf, on_delete=models.CASCADE)
    jahr = models.IntegerField(blank=True)
    vzp = models.FloatField(blank=True)
