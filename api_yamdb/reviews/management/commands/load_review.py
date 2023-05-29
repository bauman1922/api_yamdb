import datetime
from csv import DictReader

from django.core.management import BaseCommand
from django.utils.timezone import make_aware

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
                author_username = row.get('author')
                pub_date_str = row['pub_date']
                pub_date = datetime.datetime.strptime(
                    pub_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                pub_date = make_aware(pub_date)

                title = Title.objects.get(id=title_id)
                author = User.objects.filter(username=author_username).first()

                review = Review(
                    id=row['id'],
                    title=title,
                    text=row['text'],
                    author=author,
                    score=row['score'],
                    pub_date=pub_date
                )
                review.save()
                print(f"Review '{review.title}' импортирован.")

        except FileNotFoundError:
            print("CSV файл не найден.")

        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
