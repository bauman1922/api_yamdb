from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User
from .validators import validate_year


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Название категории",
        help_text="Введите название категории"
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name="Идентификатор категории",
        help_text="Создайте идентификатор для категории",
        unique=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Название жанра",
        help_text="Введите название жанра"
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name="Идентификатор жанра",
        help_text="Создайте идентификатор для жанра",
        unique=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Название произведения",
        help_text="Введите название произведения",
    )
    year = models.IntegerField(
        validators=(validate_year,),
        verbose_name="Год создания",
        help_text="Введите год создания произведения",
    )
    description = models.TextField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name="Краткое описание произведения",
        help_text="Введите краткое описание произведения"
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name="Название жанра",
        help_text="Введите название жанра"
    )
    category = models.ForeignKey(
        Category,
        related_name="titles",
        on_delete=models.SET_NULL,
        verbose_name="Название категории",
        help_text="Введите название категории",
        null=True
    )

    class Meta:
        ordering = ("category", "name")
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        verbose_name='Оценка произведения',
        validators=(
            MinValueValidator(1, 'Рейтинг не может быть меньше 1!'),
            MaxValueValidator(10, 'Рейтинг не может быть больше 10!')
        )
    )
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            )
        ]

    def __str__(self):
        return self.text[:settings.QTY_OUTPUT]


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.text[:settings.QTY_OUTPUT]
