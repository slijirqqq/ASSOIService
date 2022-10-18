from typing import AnyStr

from version.exceptions import (
    VersionDoesNotMatchSemVer,
    VersionItemMustBeDigit,
)


def validate_version(value: AnyStr) -> AnyStr:
    version_items = value.split('.')
    if len(version_items) != 3:
        raise VersionDoesNotMatchSemVer()
    for item in version_items:
        if not item.isdigit():
            raise VersionItemMustBeDigit()
    return value
