import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Strength message
    if strength == 5:
        return "Password is strong!", []
    elif 3 <= strength < 5:
        return "Password is moderate.", feedback
    else:
        return "Password is weak.", feedback

if __name__ == "__main__":
    user_password = input("Enter a password to test its strength: ")
    message, suggestions = check_password_strength(user_password)
    print(f"\n{message}")
    for suggestion in suggestions:
        print(f"- {suggestion}")
