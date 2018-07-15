from django.contrib.auth import get_user_model
from rest_framework import serializers
from project.feed.models import Profile

User = get_user_model()


class UserProfileUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=False
    )
    first_name = serializers.CharField(
        label='first_name',
        allow_blank=True,
        required=False
    )
    last_name = serializers.CharField(
        label='last_name',
        allow_blank=True,
        required=False
    )
    email = serializers.EmailField(
        label='email',
        required=False
    )
    location = serializers.CharField(
        label='location',
        required=False,
        allow_blank=False
    )
    regex = r'^\+?1?\d{9,15}$'
    phone_number = serializers.RegexField(
        label='phone_number',
        regex=regex,
        max_length=15,
        allow_blank=True,
        required=False
    )
    things_love = serializers.CharField(
        label='things_love',
        allow_blank=True,
        required=False
    )
    description = serializers.CharField(
        label='description',
        allow_blank=True,
        required=False
    )

    def validate_location(self, location):
        if location == "":
            raise serializers.ValidationError('You have to input location!')
        else:
            return location

    def validate_email(self, email):
        current_user = self.context.get('request').user
        try:
            user = User.objects.get('email')
            if user.email == current_user.email:
                raise serializers.ValidationError('This email is already registered!')
        except User.DoesNotExist:
            return email

    def validate_username(self, username):
        current_user = self.context.get('request').user
        user = User.objects.get(username=username)
        if user.username != current_user.username:
            raise serializers.ValidationError('This username is already registered!')
        else:
            return username

    def save(self, validated_data):
        user = self.context.get('request').user

        if 'email' in validated_data:
            user.email = validated_data.get('email')
        if 'username' in validated_data:
            user.username = validated_data.get('username')
        if 'first_name' in validated_data:
            user.first_name = validated_data.get('first_name')
        if 'last_name' in validated_data:
            user.last_name = validated_data.get('last_name')
        if 'location' in validated_data:
            user.profile.location = validated_data.get('location')
        if 'phone_number' in validated_data:
            user.profile.phone_number = validated_data.get('phone_number')
        if 'things_love' in validated_data:
            user.profile.things_love = validated_data.get('things_love')
        if 'description' in validated_data:
            user.profile.description = validated_data.get('description')
        user.save()
        user.profile.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['location', 'phone_number', 'things_love', 'description']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    comments_count = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    def get_comments_count(self, user):
        return user.comments.count()

    def get_reviews_count(self, user):
        return user.reviews.count()

    username = serializers.CharField(
        required=False,
        allow_blank=False
    )
    email = serializers.EmailField(
        required=True
    )

    def validate_data(self, username):
        try:
            User.object.get(username=username)
            raise serializers.ValidationError({
                'username': 'This username is already used'
            })
        except User.DoesNotExist:
            return username

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile', 'comments_count', 'reviews_count']
        read_only_fields = ['id', 'profile']
