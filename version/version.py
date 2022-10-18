from typing import (
    AnyStr,
)

from django.conf import settings


def get_api_version() -> AnyStr:
    version_file = settings.BASE_DIR / "version.txt"
    try:
        with open(version_file, "r", encoding="utf-8") as f:
            api_version = ''
            temp_lines = f.readlines()
            for line in temp_lines:
                api_version += line.strip()
    except OSError:  # pragma: no cover
        return "dev"
    return api_version
