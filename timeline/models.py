from django.db import models
from holidays.models import HolidayModel
from category.models import Category, SubCategory


class Wish(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='wishes_images')
    holiday = models.ForeignKey(HolidayModel, on_delete=models.CASCADE, related_name='gifts', null=True, blank=True)
    link = models.URLField(max_length=255, blank=True)
    description = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Подарки'

    def __str__(self):
        return self.name


class Gift(models.Model):
    KYRGYZSTAN = 'KGZ'
    KAZAKHSTAN = 'KZ'
    RUSSIA = 'RUS'
    UZBEKISTAN = 'UZ'
    COUNTRY_CHOICES = [
        (KYRGYZSTAN, 'Kyrgyzstan'),
        (KAZAKHSTAN, 'Kazakhstan'),
        (RUSSIA, 'Russia'),
        (UZBEKISTAN, 'Uzbekistan'),
    ]
    name = models.CharField(max_length=250)
    country = models.CharField(
        max_length=3,
        choices=COUNTRY_CHOICES,
        default=KYRGYZSTAN,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='gifts', null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
                                     related_name='gifts', null=True)

    CONDITION_CHOICES = [
        'New',
        'Used'
    ]
    condition = models.CharField(
        max_length=8,
        choices=CONDITION_CHOICES,
        default='New'
    )
    image = models.ImageField(upload_to='gift_image')
