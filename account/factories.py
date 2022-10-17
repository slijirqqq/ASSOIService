import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from account.choices import UserStaffChoices
from account.models import (
    PTeachingUser,
    SupportTeachingUser,
)

User = get_user_model()


class GroupFactory(factory.django.DjangoModelFactory):
    name = factory.Faker(
        "random_element",
        elements=[
            UserStaffChoices.p_teaching.value,
            UserStaffChoices.s_teaching.value,
        ]
    )

    class Meta:
        model = Group
        django_get_or_create = [
            "name"
        ]


class PTeachingUserFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("account.factories.UserFactory")

    class Meta:
        model = PTeachingUser
        django_get_or_create = [
            "user",
        ]


class SupportTeachingUserFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("account.factories.UserFactory")

    class Meta:
        model = SupportTeachingUser
        django_get_or_create = [
            "user",
        ]


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    phone = factory.Faker("msisdn", locale="ru_RU")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    middle_name = factory.Faker("name")
    password = factory.PostGenerationMethodCall("set_password", "FehKNot7")
    is_active = True

    class Meta:
        model = User
        django_get_or_create = [
            "email",
            "phone",
        ]

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:  # pragma: no cover
            return
        if extracted:
            for group in extracted:
                self.groups.add(group)
