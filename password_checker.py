"""
Password Strength Checker
Checks a password against basic security rules and gives feedback.
"""
import getpass
import string

# A few of the most commonly leaked passwords
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "password1",
    "111111", "letmein", "iloveyou", "admin", "welcome",
}


def check_password(password):
    """Return a score out of 6 and a list of improvement tips."""
    score = 0
    feedback = []

    # Length check (worth up to 2 points)
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters for a stronger password.")
    else:
        feedback.append("Too short - use at least 8 characters (12+ is better).")

    # Character variety checks (1 point each)
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add symbols like ! @ # $.")

    # Common passwords are weak no matter what
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is one of the most common passwords - never use it.")

    return score, feedback


def rating(score):
    if score >= 6:
        return "Strong"
    if score >= 4:
        return "Medium"
    return "Weak"


def main():
    # getpass hides what you type, so the password isn't shown on screen
    password = getpass.getpass("Enter a password to check (input is hidden): ")
    score, feedback = check_password(password)

    print(f"\nStrength: {rating(score)} ({score}/6)")
    for tip in feedback:
        print(f" - {tip}")


if __name__ == "__main__":
    main()