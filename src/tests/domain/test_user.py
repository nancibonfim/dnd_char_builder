import pytest
from hamcrest import assert_that, equal_to

from domain.user import User


def test_should_create_user_successfully():
    user = User.create_user("user_name", "user_email@example.com", "user_password")

    assert_that(user.name, equal_to("user_name"))
    assert_that(user.email, equal_to("user_email@example.com"))
    assert_that(user.password, user.verify_password("user_password"))


def test_should_not_create_user_with_empty_password():
    with pytest.raises(ValueError, match="Password cannot be empty"):
        User.create_user("user_name", "user_email@example.com", "")


def test_should_hash_password():
    user = User.create_user("user_name", "user_email@example.com", "user_password")

    assert_that(user.verify_password("user_password"), equal_to(True))
