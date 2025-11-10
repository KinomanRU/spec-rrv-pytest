import string

SPECIAL = "_!@#$%^&"
ATTEMPTS_NUM = 5
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 15


def check_password(password: str) -> tuple[bool, str]:
    if not password:
        return False, "Empty password."
    pass_len = len(password)
    if pass_len < MIN_PASSWORD_LENGTH:
        return (
            False,
            f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.",
        )
    if pass_len > MAX_PASSWORD_LENGTH:
        return False, f"Password must be at most {MAX_PASSWORD_LENGTH} characters long."

    message = ""
    digits_flag = False
    lowercase_flag = False
    uppercase_flag = False
    special_flag = False
    for c in password:
        if c in string.digits:
            digits_flag = True
        if c in string.ascii_lowercase:
            lowercase_flag = True
        if c in string.ascii_uppercase:
            uppercase_flag = True
        if c in SPECIAL:
            special_flag = True

    if not digits_flag:
        message += "Password must contain at least one digit.\n"
    if not lowercase_flag:
        message += "Password must contain at least one lowercase letter.\n"
    if not uppercase_flag:
        message += "Password must contain at least one uppercase letter.\n"
    if not special_flag:
        message += "Password must contain at least one special character.\n"
    if message:
        return False, message
    return True, ""


def main():
    for i in range(1, ATTEMPTS_NUM + 1):
        password: str = input("Enter your password: ")
        check, message = check_password(password)
        if check:
            print(f"Attempt {i}. Password is VALID.")
            break
        print(f"Attempt {i}. Password is INVALID: {message}")
    else:
        print("Access denied.")
        return
    print("Access granted.")


if __name__ == "__main__":
    main()
