from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from .utils import send_activation_email

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirmation']

    def validation_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with given email already exists')
        return email

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirmation = validated_data.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(email, password)
        send_activation_email(user.email, user.activation_code)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs