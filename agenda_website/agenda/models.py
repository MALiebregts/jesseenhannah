from django.db import models

class AgendaItem(models.Model):
    datum = models.DateField()
    tijdstip = models.TimeField()
    omschrijving = models.CharField(max_length=200)
    kosten = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.omschrijving} op {self.datum} om {self.tijdstip}"
