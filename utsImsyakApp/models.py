from django.db import models

# Create your models here.
class jadwalModels(models.Model):
    Tanggal = models.CharField(max_length=50)
    Imsyak = models.TimeField()
    Subuh = models.TimeField()
    Terbit = models.TimeField()
    Duha = models.TimeField()
    Zuhur = models.TimeField()
    Asar = models.TimeField()
    Magrib = models.TimeField()
    Isya = models.TimeField()

    def __str__(self):
        return self.Tanggal