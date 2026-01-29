
import string

def load_dictionary_words():
    """
    Placeholder function to load common dictionary words.
    In a real application, you would read a file like 'dictionary.txt'.
    Returns a set of lowercase words for efficient case-insensitive lookups.
    """
    # Example list: replace with actual file reading logic
    common_words = ["password", "123456", "qwerty"]
    return set(word.lower() for word in common_words)

def load_top_passwords():
    """
    Placeholder function to load top used passwords.
    In a real application, you would read a file like 'toppasswords.txt'.
    Returns a set for efficient case-sensitive lookups.
    """
    # Example list: replace with actual file reading logic
    top_passwords = {"password", "12345678", "Password123"}
    return set(top_passwords)

def check_password_strength(password: str):
    """
    Evaluates password strength based on the provided rules.
    Returns the strength value (0, 1, or 5) and prints the corresponding message.
    """
    dictionary_words = load_dictionary_words()
    top_passwords_list = load_top_passwords()
    
    # 5.1 If the password is in the dictionary file (case-insensitive match)
    if password.lower() in dictionary_words:
        print("Password is a dictionary word and is not secure.")
        return 0
    
    # 5.2 If the password is in the toppassword list (case-sensitive match)
    if password in top_passwords_list:
        print("Password is a commonly used password and is not secure.")
        return 0
    
    # 5.3 If the password is shorter than the minimum password length of 10
    if len(password) < 10:
        print("Password is too short and is not secure.")
        return 1
    
    # 5.4 If the password is longer than 15 characters, the password is strong
    if len(password) > 15:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    # 5.5 For the remainder of the cases, determine strength by complexity
    # Complexity score is 1 to 4 based on character types used
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    # Special symbols are all printable characters that are not alphanumeric
    has_special = any(char in string.punctuation for char in password)
    
    complexity_score = sum([has_upper, has_lower, has_digit, has_special])
    
    print(f"Password complexity score is {complexity_score}.")
    return complexity_score

# --- Example Usage ---
test_passwords = [
    "password",         # Dictionary word (case-insensitive)
    "Password123",      # Top password (case-sensitive)
    "short",            # Too short
    "Averylongpasswordthatisfifteencharacters", # Exactly 40 chars, > 15
    "LengthyButSimple1", # Between 10 and 15, complexity 2
    "ComplexP@ssw0rd!"   # Between 10 and 15, complexity 4
]

for pwd in test_passwords:
    print(f"\nChecking password: '{pwd}'")
    strength = check_password_strength(pwd)
    print(f"Returned strength value: {strength}")