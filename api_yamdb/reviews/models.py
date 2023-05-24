from django.db import models


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
        through="GenreTitle",
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


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE)
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.genre} {self.title}'
