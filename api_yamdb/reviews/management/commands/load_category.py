from csv import DictReader

from django.core.management import BaseCommand

from reviews.models import Category

ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из файла CSV,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py migrate` для нового пустого
база данных с таблицами"""


class Command(BaseCommand):
    help = "Выгрузка данных из category.csv"

    def handle(self, *args, **options):
        if Category.objects.exists():
            print("Данные уже загружены...выход!")
            print(ERROR_MESSAGE)
            return
        print("Загрузка Category данных")

        try:
            for row in DictReader(open("static/data/category.csv")):
                category = Category(id=row['id'], name=row['name'],
                                    slug=row['slug'])
                category.save()
                print(f"Category '{category.name}' импортирован.")
        except FileNotFoundError:
            print("CSV file не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
