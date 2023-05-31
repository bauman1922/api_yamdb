import datetime
from csv import DictReader

from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand

from reviews.models import Review, Title
from users.models import User

ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из файла CSV,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py migrate` для новой пустой
базы данных с таблицами"""


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
                title_id = row['title_id']
                author_id = row.get('author')
                pub_date_str = row['pub_date']
                pub_date = datetime.datetime.strptime(
                    pub_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                title = Title.objects.get(id=title_id)

                try:
                    author = User.objects.get(id=author_id)
                except ObjectDoesNotExist:
                    print(f"Пользователь с идентификатором {author_id}"
                          "не найден")
                    continue
                review = Review.objects.create(
                    title=title,
                    text=row['text'],
                    author=author,
                    score=row['score'],
                    pub_date=pub_date
                )
                review.save()
                print(f"Genre'{review.title}' импортирован.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
