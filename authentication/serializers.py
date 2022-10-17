from typing import AnyStr

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.choices import UserStaffChoices
from account.models import (
    PTeachingUser,
    SupportTeachingUser,
)
from app_core.serializers import SerializersImplMixin
from authentication.exceptions import IncorrectPasswordError
from authentication.validators import validate_password

User = get_user_model()


class ASSOITokenObtainPairSerializer(SerializersImplMixin, TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializer, cls).get_token(user)

        token['email'] = user.email
        token['roles'] = list(user.groups.all().values_list('name', flat=True))

        return token


class RegistrationSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(
        source="groups",
        slug_field="name",
        queryset=Group.objects.exclude(name=UserStaffChoices.admin.value),
        many=True,
    )

    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "first_name",
            "last_name",
            "middle_name",
            "role",
            "password",
        ]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "validators": [validate_password],
            },
            "phone": {
                "initial": None,
            }
        }

    @staticmethod
    def validate_phone(value: AnyStr):
        if value == "":
            return None
        return value

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data.get("password"))
        self.create_relation(user)
        user.save()
        return user

    @staticmethod
    def create_relation(user):
        group_mapping = {
            UserStaffChoices.s_teaching.value: SupportTeachingUser,
            UserStaffChoices.p_teaching.value: PTeachingUser,
        }
        user_groups = user.groups.all()
        for group in user_groups:
            if group.name not in group_mapping:
                continue
            group_mapping[group.name].active_objects.create(user=user)


class PasswordChangeSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "new_password",
            "old_password",
        ]
        extra_kwargs = {
            "new_password": {
                "source": "password",
                "write_only": True,
                "validators": [validate_password]
            },
            "old_password": {
                "write_only": True,
            }
        }

    def validate_old_password(self, value):
        if not self.instance.check_password(value):
            raise IncorrectPasswordError()
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("password"))
        return instance
