import re
import validation_functions as vf


if __name__ == "__main__":

    # Task 1
    print(f"{'Task #1':-^60}")

    text_to_check = "ssgsgRbbbbbrsfsfsRBR"
    pattern = r"[Rr][Bb]+[Rr]"
    res = re.findall(pattern, text_to_check)
    if res:
        print(res)
    else:
        print("Pattern not found")

    # Task 2
    print(f"{'Task #2':-^60}")

    card_number_1 = "9999-9999-9999-9999"
    # card_number_2 = "9999999999999999"
    # card_number_3 = "9999 9999 9999 9999"
    # card_number_4 = "oooo-9999-9999-9999"

    print(vf.card_number_validation(card_number_1))
    # print(vf.card_number_validation(card_number_2))
    # print(vf.card_number_validation(card_number_3))
    # print(vf.card_number_validation(card_number_4))

    # Task 3
    print(f"{'Task #3':-^60}")

    email_1 = "simple@example.com"
    email_2 = "fully-qualified-domain@example.com"
    email_3 = "user--example.com@example.org"
    email_4 = "-user-example.com@example.org"
    print(vf.email_validation(email_1))
    print(vf.email_validation(email_2))
    print(vf.email_validation(email_3))
    print(vf.email_validation(email_4))

    # Task 4
    print(f"{'Task #4':-^60}")

    login_to_check_1 = "Login12"
    login_to_check_2 = "dfd120sdsdw"
    print(vf.login_validation(login_to_check_1))
    print(vf.login_validation(login_to_check_2))
