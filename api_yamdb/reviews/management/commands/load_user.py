from csv import DictReader

from django.core.management import BaseCommand

from users.models import User

ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из файла CSV,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py migrate` для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Выгрузка данных из users.csv"

    def handle(self, *args, **options):
        if User.objects.exists():
            print("Данные уже загружены...выход!")
            print(ERROR_MESSAGE)
            return
        print("Загрузка Users данных")

        try:
            for row in DictReader(open('static/data/users.csv')):
                user = User(id=row['id'], username=row['username'],
                            email=row['email'], role=row['role'],
                            bio=row['bio'], first_name=row['first_name'],
                            last_name=row['last_name'])
                user.save()
                print(f"Users '{user.username}' импортирован.")
        except FileNotFoundError:
            print("CSV file не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
