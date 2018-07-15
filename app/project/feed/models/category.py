from django.db import models


class Category(models.Model):

    name = models.CharField(
        verbose_name='category_name',
        max_length=20,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
