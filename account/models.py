from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse
from account import managers

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    email = models.CharField(
        db_column='tx_email',
        max_length=256,
        null=False,
        unique=True,
    )
    password = models.CharField(
        db_column='tx_password',
        max_length=104,
        null=False
    )
    full_name = models.CharField(
        db_column='tx_name',
        max_length=256,
        null=False
    )
    last_login = models.DateTimeField(
        db_column='dt_last_login',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    is_superuser = models.BooleanField(
        db_column='cs_superuser',
        null=True,
        default=False
    )
    is_staff = models.BooleanField(
        db_column='cs_staff',
        null=True,
        default=False
    )

    objects = managers.UserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.id})
    
    class Meta:
        managed = True
        db_table = 'tb_auth_user'


class UserAdress(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        db_column='id_user',
        db_index=False,
        null=False,
        related_name='user_adresses',
        verbose_name='User'
    )
    adress = models.TextField(
        db_column='tx_adress',
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Adress'
    )
    city = models.CharField(
        db_column='tx_city',
        max_length=50,
        null=False,
        blank=False,
        verbose_name='City'
    )
    country = models.CharField(
        db_column='tx_country',
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Country'
    )
    postal_code = models.CharField(
        db_column='tx_postal_code',
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Postal Code'
    )
    phone = models.CharField(
        db_column='tx_phone',
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Phone'
    )
    def __str__(self):
        return f'Adress - {self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('adress-detail', kwargs={'pk': self.id})
    
    objects = managers.UserAdressManager()

    class Meta:
        managed = True
        db_table = 'tb_adress'





