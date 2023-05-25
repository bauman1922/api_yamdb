from rest_framework import serializers
from reviews.models import Category, Genre, GenreTitle, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(
    #     slug_field='username',
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )
    # following = serializers.SlugRelatedField(
    #     slug_field='username',
    #     queryset=User.objects.all()
    # )

    class Meta:
        model = Title
        fields = '__all__'

    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset=Follow.objects.all(),
    #             fields=('user', 'following')
    #         )
    #     ]

    # def validate(self, data):
    #     if self.context.get('request').user == data.get('following'):
    #         raise serializers.ValidationError(
    #             'Невозможно оформить подписку на самого себя!')
    #     return data


class GenreTitleSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(
    #     slug_field='username', read_only=True)

    class Meta:
        model = GenreTitle
        fields = '__all__'
