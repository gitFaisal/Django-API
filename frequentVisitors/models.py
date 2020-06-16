from django.db import models

class VisitorsTable(models.Model):
    personId = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    visits = models.IntegerField()

    class Meta:
        verbose_name_plural = "Visitors"

    def __str__(self):
        return self.first_name
