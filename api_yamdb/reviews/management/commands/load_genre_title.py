from csv import DictReader

from django.core.management.base import BaseCommand

from reviews.models import Genre, Title


class Command(BaseCommand):
    help = "Выгрузка данных из genre_title.csv"

    def handle(self, *args, **options):
        if not Title.objects.exists() or not Genre.objects.exists():
            print("Отсутствуют данные для моделей Title и Genre...выход!")
            return
        print("Загрузка Genre_Title данных")

        try:
            for row in DictReader(open('static/data/genre_title.csv')):
                title_id = row['title_id']
                genre_id = row['genre_id']
                try:
                    genre = Genre.objects.get(id=genre_id)
                    title = Title.objects.get(id=title_id)
                    if not title.genre.filter(id=genre_id).exists():
                        title.genre.add(genre)
                        print(f"Genre_Title '{title}' импортирован.")
                    else:
                        print(f"Genre_Title '{title}' уже существует.")
                except Genre.DoesNotExist:
                    print(f"Жанр с ID {genre_id} не существует.")
                except Title.DoesNotExist:
                    print(f"Произведение с ID {title_id} не существует.")
        except FileNotFoundError:
            print("CSV file не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
