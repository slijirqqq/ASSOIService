import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    phone = factory.Faker("msisdn", locale="ru_RU")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall("set_password", "FehKNot7")
    is_active = True

    class Meta:
        model = get_user_model()
        django_get_or_create = [
            "email",
            "phone",
        ]
