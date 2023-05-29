from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Genre, GenreTitle, Title

ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из файла CSV,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py migrate` для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Выгрузка данных из genre_title.csv"

    def handle(self, *args, **options):
        if GenreTitle.objects.exists():
            print("Данные уже загружены...выход!")
            print(ERROR_MESSAGE)
            return
        print("Загрузка Genre_Title данных")

        try:
            for row in DictReader(open('static/data/genre_title.csv')):
                title_id = row['title_id']
                genre_id = row['genre_id']
                genre = Genre.objects.get(id=genre_id)
                title = Title.objects.get(id=title_id)
                genre_title = GenreTitle(id=row['id'], title=title,
                                         genre=genre)
                genre_title.save()
                print(f"Genre_Title '{genre_title.title}' импортирован.")
        except FileNotFoundError:
            print("CSV file не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
