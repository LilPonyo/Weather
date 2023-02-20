from django.db import models


class Users(models.Model):
    name = models.CharField('Имя', max_length=50)
    password = models.CharField('пароль', max_length=250)
    phone = models.CharField('Phone', max_length=20)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Юзера'
        verbose_name_plural = 'Юзеры'