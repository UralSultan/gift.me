from django.db import models


class HolidayModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='holiday_image')
    date_of_holiday = models.DateField()

    class Meta:
        verbose_name_plural = 'holidays'

    def __str__(self):
        return self.name
