import csv
from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Title

DATA = {
    # Category: 'category.csv',
    Title: 'titles.csv',
    # Genre: 'genre.csv',
    # GenreTitle: 'genre_title.csv',
    # Review: 'review.csv',
    # Comment: 'comments.csv',
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        for model, file in DATA.items():
            with open(
                    f'{settings.BASE_DIR}/static/data/{file}',
                    'r', encoding='utf-8',
            ) as file_csv:
                reader = csv.DictReader(file_csv)
                model.objects.bulk_create(model(**data) for data in reader)

        self.stdout.write(self.style.SUCCESS('Данные загружены'))
