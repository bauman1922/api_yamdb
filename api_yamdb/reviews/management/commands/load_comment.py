import datetime
from csv import DictReader

from django.core.management import BaseCommand
from django.utils.timezone import make_aware

from reviews.models import Comment, Review
from users.models import User

ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из файла CSV,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py migrate` для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Выгрузка данных из comments.csv"

    def handle(self, *args, **options):
        if Comment.objects.exists():
            print("Данные уже загружены...выход!")
            print(ERROR_MESSAGE)
            return
        print("Загрузка Comments данных")

        try:
            for row in DictReader(open('static/data/comments.csv')):
                review_id = row['review_id']
                author_id = row['author']
                pub_date_str = row['pub_date']
                pub_date = datetime.datetime.strptime(
                    pub_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                pub_date = make_aware(pub_date)

                review = Review.objects.get(id=review_id)
                author = User.objects.get(id=author_id)

                comment = Comment(
                    review=review,
                    text=row['text'],
                    author=author,
                    pub_date=pub_date
                )
                comment.save()
                print(f"Comment '{comment.review}' импортирован.")

        except FileNotFoundError:
            print("CSV файл не найден.")

        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
