from csv import DictReader

from django.core.management import BaseCommand

from reviews.models import Category, Title

ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из файла CSV,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py migrate` для нового пустого
база данных с таблицами"""


class Command(BaseCommand):
    help = "Выгрузка данных из titles.csv"

    def handle(self, *args, **options):
        if Title.objects.exists():
            print("Данные уже загружены...выход!")
            print(ERROR_MESSAGE)
            return
        print("Загрузка Titles данных")

        try:
            for row in DictReader(open('static/data/titles.csv')):
                category_id = row['category']
                category = Category.objects.get(id=category_id)
                title = Title(id=row['id'], name=row['name'],
                              year=row['year'], category=category)
                title.save()
                print(f"Title '{title.name}' импортирован.")
        except FileNotFoundError:
            print("CSV file не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
