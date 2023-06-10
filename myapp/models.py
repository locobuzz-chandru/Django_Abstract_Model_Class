from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=12)


class NineManager(models.Manager):
    def get_queryset(self):
        return super(NineManager, self).get_queryset().filter(phone__startswith='9')


class EightManager(models.Manager):
    def get_queryset(self):
        return super(EightManager, self).get_queryset().filter(phone__startswith='8')


class SevenManager(models.Manager):
    def get_queryset(self):
        return super(SevenManager, self).get_queryset().filter(phone__startswith='7')


class Nine(Contact):
    objects = NineManager()

    class Meta:
        proxy = True


class Eight(Contact):
    objects = EightManager()

    class Meta:
        proxy = True


class Seven(Contact):
    objects = SevenManager()

    class Meta:
        proxy = True
