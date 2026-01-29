def main ():
    """Entry point for the program"""
    print("WElcome to the password checker")
    password = str(input("Please enter a password:"))
    
    #Call the function to check password strength
    strength = check_password_strength(password)
    
    print (f"Your password strength is :{strength}")

def check_password_strength(password: str):
    
    """
    Evaluates password strength based on length , casing ,digits,
    and symbols.
    """    
    
    #Criteria flags.
    has_upper =False
    has_lower =False
    has_digit =False
    has_special =False
    
    special_characters ="!@#$%^&*()-_=+{}[]|:;,.<>?/"
    
    #Check length
    if len(password) < 8:
        return "weak (Too short)"
    
    #Iterate through characters to check requirements
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # scoring Logic
    criteria_met = [has_upper, has_lower, has_digit, has_special]
    score = sum(criteria_met)
    if score == 4:
        return "strong"
    elif score >= 2:
        return "medium"
    else:
        return "weak"
        
        #start the program
        if_name_=="_main_"
        main()
        
        
        
