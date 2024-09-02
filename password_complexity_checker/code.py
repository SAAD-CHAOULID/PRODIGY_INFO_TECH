
import re

def is_sequential(password):
    # Check if the password contains any sequential letters or numbers.
    sequences = ['abcdefghijklmnopqrstuvwxyz', '0123456789']
    for seq in sequences:
        for i in range(len(password) - 3):
            if password[i:i+4].lower() in seq:
                return True
    return False

def check_password_complexity(password):
    # Initialize the complexity score and feedback list
    global feedback
    complexity = 0
    feedback = ""
    # Check the length of the password
    if len(password) >= 10:
        complexity += 2
    elif len(password) >= 8:
        complexity += 1
    else:
        feedback += "8 characters long. \n"
        
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        complexity += 1
    else:
        feedback += "one uppercase letter. \n"
        
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        complexity += 1
    else:
        feedback += "one lowercase letter. \n"
        
    # Check for digits
    if re.search(r'[0-9]', password):
        complexity += 1
    else:
        feedback += "one digit. \n"
        
    # Check for special characters
    if re.search(r'[@#$%^&+=!:;,?.\\*/`]', password):
        complexity += 2
    else:
        feedback += "one special character . \n"

    # Check for a space
    if re.search(r' ', password):
        complexity += 2
    else :
        feedback += "one space. \n"
    
    # Check for sequential patterns
    if is_sequential(password) :
        complexity -= 2
        feedback += "should not contain sequential characters (e.g., 'abcd', '1234')."

    # Determine the complexity level
    if complexity >= 8:
        return "highly secure"
    elif complexity >= 6:
        return "secure"
    elif complexity >= 4:
        return "moderate"
    else:
        return "weak"


tips = '''
    Here are some quick tips for creating a secure password:
    1. Length: Aim for at least 12 characters.
    2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.
    3. Avoid Common Words: Don't use easily guessable information.
    4. No Personal Info: Avoid using names, birthdays, or personal details.
    5. Use Passphrases: Consider combining multiple words or a sentence.
    6. Unique for Each Account: Don't reuse passwords across multiple accounts.
    7. Regular Updates: Change passwords periodically.
    8. Enable 2FA: Use Two-Factor Authentication where possible.
    9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.
    10. Password Manager: Consider using one for secure and unique passwords
'''
if __name__ == '__main__':
    print("Welcome to your password complexity checker", tips)
    password = input("  Please enter your password :  ")
    print("Your password is ", check_password_complexity(password))
    if feedback :
        print("Your password should contains at least:\n", feedback)

