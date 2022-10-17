from dataclasses import dataclass
from typing import AnyStr

from app_core.dataclasses import DataclassMixin
from app_core.faker import fake


@dataclass
class AuthenticationDataclass(DataclassMixin):
    email: AnyStr = fake.email()
    password: AnyStr = fake.password()


@dataclass
class RefreshTokenDataclass(DataclassMixin):
    refresh: AnyStr
