from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Review, Title

ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из файла CSV,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py migrate` для нового пустого
база данных с таблицами"""


class Command(BaseCommand):
    help = "Выгрузка данных из review.csv"

    def handle(self, *args, **options):
        if Review.objects.exists():
            print("Данные уже загружены...выход!")
            print(ERROR_MESSAGE)
            return
        print("Загрузка Review данных")

        try:
            for row in DictReader(open('static/data/review.csv')):
                title_id = row['title']
                title = Title.objects.get(id=title_id)
                review = Review(id=row['id'], title=title, text=row['text'],
                                author=row['author'], score=row['score'],
                                pub_date=row['pub_date'])
                review.save()
                print(f"Review '{review.title}' импортирован.")
        except FileNotFoundError:
            print("CSV file не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
