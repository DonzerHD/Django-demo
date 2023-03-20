from django.db import models

# Create your models here.

class Functionnality(models.Model):
    class Meta:
        verbose_name_plural = "Functionnalities"

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=500,
        null=False,
        blank=False,
    )
    
    def __str__(self):
        return f"{self.name} - {self.description}"