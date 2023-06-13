import string
import random

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


def generate_code(symbols_number: int = 10):
    return ''.join(random.sample(string.ascii_letters, symbols_number))


class Test(models.Model):
    login_code = models.CharField(
        default=generate_code,
        max_length=10,
        db_index=True,
        unique=True,
        editable=False,
        verbose_name='Уникальный логин-код',
    )

    class Meta:
        verbose_name = 'Логин'
        verbose_name_plural = 'Логины'

    def __str__(self):
        return self.login_code


class BaseTest(models.Model):
    test = models.OneToOneField(Test, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s")
    completed_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name='Время прохождения теста'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.test)


class EQ(BaseTest):
    results = models.CharField(max_length=5, verbose_name='Результаты EQ-теста')

    class Meta:
        verbose_name = 'EQ-тест'
        verbose_name_plural = 'EQ-тесты'


class IQ(BaseTest):
    results = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        verbose_name='Результаты IQ-теста'
    )

    class Meta:
        verbose_name = 'IQ-тест'
        verbose_name_plural = 'IQ-тесты'
