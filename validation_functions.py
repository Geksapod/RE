import re


def card_number_validation(card_number: str):
    """
    Return True if card number contain 16 digits, every 4 digits are split by "-"
    Example: 9999-9999-9999-9999 is valid card number.
    """

    card_number_pattern_1 = r"(\d{4}-){3}\d{4}"
    # card_number_pattern_2 = r"\d{16}"

    if re.fullmatch(card_number_pattern_1, card_number):
        return True
    # if re.fullmatch(card_number_pattern_2, card_number):
    #     return True


def email_validation(email: str):
    """
    Return True if email address is valid.
    Valid email address consists of local-part and domain separated by "@".

    Local-part requirements:
    - uppercase and lowercase Latin letters A to Z and a to z
    - digits 0 to 9
    - printable characters -_, provided that it is not the first or last character and
      provided also that it does not appear consecutively
    - dot ., provided that it is not the first or last character and
      provided also that it does not appear consecutively (e.g., John..Doe@example.com is not allowed).

    Domain requirements:
    - uppercase and lowercase Latin letters A to Z and a to z;
    - digits 0 to 9, provided that top-level domain names are not all-numeric;
    - hyphen -, provided that it is not the first or last character.

    Examples:

    Valid email addresses
        simple@example.com
        very.common@example.com
        disposable.style.email.with+symbol@example.com
        other.email-with-hyphen@example.com
        fully-qualified-domain@example.com

    Invalid email addresses
        Abc.example.com (no @ character)
        A@b@c@example.com (only one @ is allowed outside quotation marks)
        --very.common@example.com
    """

    email_pattern = r"(\w+[-_.]?\w+)+@(\w+.)+[A-Za-z]+"
    res = re.match(email_pattern, email)
    if res:
        return True


def login_validation(login: str):
    """
    Return True if login is valid.

    Valid login may use any of these ASCII characters:
    - uppercase and lowercase Latin letters A to Z and a to z
    - digits 0 to 9
    Length of valid login from 2 to 10 characters.
    """

    login_pattern = r"\w{2,10}"
    if re.fullmatch(login_pattern, login):
        return True
