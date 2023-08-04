import re
import unittest


def validate_email(email: str) -> bool:
    """
    Validate an email address based on specific rules.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    # Proper email format check
    if not re.match(r"^\S+@\S+\.\S+$", email):
        return False

    # Valid email providers check
    valid_providers = ["yahoo", "gmail", "outlook"]
    email_provider = email.split("@")[1].split(".")[0]
    if email_provider not in valid_providers:
        return False

    # No disposable email providers check
    if "yopmail" in email:
        return False

    return True


class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(validate_email("john.doe@gmail.com"))
        self.assertTrue(validate_email("jane.smith@yahoo.com"))
        self.assertTrue(validate_email("michael.scott@outlook.com"))

    def test_invalid_emails(self):
        self.assertFalse(validate_email("invalid-email"))
        self.assertFalse(validate_email("john.doe@invalid.com"))
        self.assertFalse(validate_email("jane.smith@yopmail.com"))
        self.assertFalse(validate_email("michael.scott@disposable.com"))


if __name__ == "__main__":
    unittest.main()
