from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


class Students(models.Model):
    GENDERS = (
        ('1', _('Female')),
        ('2', _('Male')),
        ('3', _('Other')),
        ('4', _('Prefer to not say')),
    )
    username_validator = UnicodeUsernameValidator()
    first_name = models.CharField(max_length=200, verbose_name=_('first name'))
    last_name = models.CharField(max_length=200, verbose_name=_('last name'))
    email = models.EmailField(max_length=254, verbose_name=_('email'), unique=True, validators=[username_validator])
    phone = models.CharField(max_length=15, verbose_name=_('phone number'), unique=True)
    gender = models.CharField(max_length=15, choices=GENDERS, verbose_name=_('genders'))
    number = models.PositiveIntegerField(verbose_name=_('number'), )
    image = models.ImageField(verbose_name=_('image'), upload_to='students/%Y/%m/%d/', default='students/avatar.png')
