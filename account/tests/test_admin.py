from typing import List

from django.contrib.admin import AdminSite
from django.test import TestCase

from account.admin import (
    PTSAdmin,
    STSAdmin,
)
from account.choices import UserStaffChoices
from account.factories import (
    UserFactory,
    GroupFactory, PTeachingUserFactory, SupportTeachingUserFactory,
)
from account.models import (
    PTeachingUser,
    SupportTeachingUser,
)


class TestUserAdmin(TestCase):

    def setUp(self) -> None:
        self.setUpGroups()
        self.pts_user = UserFactory.create(groups=[self.pts_group])
        self.sts_user = UserFactory.create(groups=[self.sts_group])
        self.pts_instance = PTeachingUserFactory.create(user=self.pts_user)
        self.sts_instance = SupportTeachingUserFactory.create(user=self.sts_user)
        self.pts_admin = PTSAdmin(PTeachingUser, AdminSite())
        self.sts_admin = STSAdmin(SupportTeachingUser, AdminSite())

    def setUpGroups(self):
        self.pts_group = GroupFactory.create(name=UserStaffChoices.p_teaching.value)
        self.sts_group = GroupFactory.create(name=UserStaffChoices.s_teaching.value)

    def test_display_list(self):
        user_mapping = {
            self.pts_instance: self.pts_admin,
            self.sts_instance: self.sts_admin,
        }
        for user in [self.pts_instance, self.sts_instance]:
            admin_model = user_mapping[user]
            first_name = admin_model.get_first_name(user)
            last_name = admin_model.get_last_name(user)
            middle_name = admin_model.get_middle_name(user)
            phone = admin_model.get_phone(user)
            email = admin_model.get_email(user)
            displays = [
                first_name,
                last_name,
                middle_name,
                phone,
                email,
            ]

            self.assertDisplayEquals(user, displays)

    def assertDisplayEquals(self, user, displays: List):
        self.assertListEqual(
            [
                user.user.first_name,
                user.user.last_name,
                user.user.middle_name,
                user.user.phone,
                user.user.email,
            ],
            displays,
        )
