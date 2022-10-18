from dataclasses import dataclass
from typing import AnyStr

from app_core.dataclasses import DataclassMixin


@dataclass
class VersionDataclass(DataclassMixin):
    version: AnyStr
