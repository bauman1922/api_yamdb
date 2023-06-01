from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User
from users.validators import validate_username


class SignUpSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
        max_length=50,
        validators=[validate_username]
    )
    email = serializers.EmailField(
        required=True,
        max_length=200
    )

    def validate(self, data):

        filter_user_email = User.objects.filter(username=data['username'],
                                                email=data['email']).exists()
        filter_user = User.objects.filter(username=data['username']).exists()
        filter_email = User.objects.filter(email=data['email']).exists()

        if filter_user_email:
            return data
        if filter_email or filter_user:
            raise serializers.ValidationError(
                'Такой пользователь уже есть'
            )
        return data


class TokenSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
        max_length=50,
        validators=[validate_username]
    )
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=True,
        max_length=50,
        validators=[validate_username,
                    UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        max_length=200,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )


class UserMeSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        read_only_fields = ('role',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id',)


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        fields = (
            'id', 'name', 'year', 'description', 'genre', 'category'
        )
        model = Title

    def validate_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError('Год выпуска '
                                              'не может быть больше текущего!')
        return value


class TitleListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def validate(self, data):
        if self.context['request'].method == 'POST':
            reviewer = self.context['request'].user
            title_id = self.context['view'].kwargs['title_id']
            if Review.objects.filter(author=reviewer,
                                     title_id=title_id).exists():
                raise serializers.ValidationError(
                    'Нельзя оставить отзыв на одно произведение дважды!'
                )

        if not 1 <= data['score'] <= 10:
            raise serializers.ValidationError(
                'Оценка может быть от 1 до 10!'
            )

        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
