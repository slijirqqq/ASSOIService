from dataclasses import dataclass
from typing import AnyStr

from django.contrib.contenttypes.models import ContentType

APP_LABELS = [
    "geo",
    "account",
    "academic",
]


@dataclass
class ModelPermission:
    code_name: AnyStr
    name: AnyStr
    content_type: ContentType
