from typing import List

from account.choices import UserStaffChoices
from account.models import (
    User,
    PTeachingUser,
    SupportTeachingUser,
)


def set_user_to_relation(user: User, roles: List) -> None:
    """
    Set user relation with belongs of group
    :param user: User instance
    :param roles: List of groups
    :return: None
    """
    group_mapping = {
        UserStaffChoices.s_teaching.value: SupportTeachingUser,
        UserStaffChoices.p_teaching.value: PTeachingUser,
    }
    for group in roles:
        if group.name not in group_mapping:
            continue
        group_mapping[group.name].active_objects.create(user=user)
