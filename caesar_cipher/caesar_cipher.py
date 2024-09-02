#create the encryption funtion
def encrypt(message,shift) :
    encrypted_message = ""
    for letter in message : 
        if letter.isalpha() :    #Check if the character is a letter to encrypt it
            base = 65 if letter.isupper() else 97    #The first uppercase letter is 'A', which has an ASCII value of 65 and he first lowercase letter is 'a', which has an ASCII value of 97.
            encrypted_letter = chr((ord(letter) - base + shift) % 26 + base)   #Convert the letter to its ASCII value with ord(), subtract the base to get a zero-based index, add the shift value, use modulo 26 to wrap around the alphabet, add the base back to convertto the correct ASCII value, and finally use chr() to convert the ASCII value back to a character.
        else :
            encrypted_letter = letter    #Non-alphabetic characters are added directly without encryption
        encrypted_message += encrypted_letter   
    return encrypted_message

#create the decryption function
def decrypt(message,shift) :
    decrypted_message = ""
    for letter in message :
        if letter.isalpha() :   #Same as in the encryption
            base = 65 if letter.isupper() else 97   
            decrypted_letter = chr((ord(letter) - base - shift) % 26 + base)    #Here we substract the shift value instead of adding it
        else :
            decrypted_letter = letter   #Same as in the encryption
        decrypted_message += decrypted_letter
    return decrypted_message

# Main code to get user input and perform encryption or decryption

message = input("insert the message you want to encrypt or decrypt : ")
question = ""   #initiate the question with character different from 'e' and 'd' to enter the loop below

while question != 'e' and question != 'd':   #Don't exit the loop till the user types 'e' or 'd'
    question = input("If you want to encrypt the message, type 'e'. If you want to decrypt it, type 'd': ")

shift = int(input("insert the shift value for the encryption or the decryption : "))

if question == 'e' :
    print("The encrypted message is : ", encrypt(message,shift))
elif question == 'd' :
    print("The decrypted message is : ", decrypt(message,shift))
