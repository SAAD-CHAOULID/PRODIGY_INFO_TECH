#Click on the 3 points next to the file name to see the description

from PIL import Image
import numpy as np


def encrypt_img(img_path) :  
    public_key = np.random.randint(0, 256)       #  Generate a random public key

    while public_key % 2 == 0:   # Check if the number is even
        public_key = np.random.randint(0, 256)  # Generate a new number if even

    print("Your public key is : ", public_key)
    
    private_key = 0      #Initiate the private key with a value of 0 to enter the loop
    while private_key % 2 == 0:    # Check if the number is even
        private_key = int(input("Enter your private key. It should be odd : "))      #  Prompt user to enter their private key

    img = Image.open(img_path)      # Open the image using PIL

    # Convert the image to a NumPy array (3D array: height x width x color channels)
    img_array = np.array(img)

    height, width, channels = img_array.shape


    # First layer of encryption: Adjust color values using the private key :
    for y in range(height) :
        for x in range(width) :
            r,g,b = img_array[y,x]
            r = (r + private_key - 100) % 256
            g = (g + private_key) % 256
            b = (b + private_key + 150) % 256
            img_array[y, x] = [r, g, b]


    # Second layer of encryption: Apply different operations to every third pixel using the private or public key :
    for y in range(height) :
        for x in range(0,int(width - 1), 3) :
            r,g,b = img_array[y,x]
            r = (r * private_key) % 256
            g = (g * private_key) % 256
            b = (b * private_key) % 256
            img_array[y, x] = [r, g, b]
        
        for x in range(0,int(width - 1), 3) :
            r,g,b = img_array[y,x + 1]
            r = (r * public_key) % 256
            g = (g - public_key) % 256
            b = (b - public_key) % 256
            img_array[y, x + 1] = [r, g, b]


    # Third layer of encryption: Swap pixels in groups of 10 :
    for y in range(height) :
        for x in range(0,int(width - 10), 10) :
            img_array[y,x],img_array[y,x + 8] = img_array[y,x + 8],img_array[y,x]
            img_array[y,x + 9],img_array[y,x + 5] = img_array[y,x + 5],img_array[y,x + 9]
            img_array[y,x + 2],img_array[y,x + 7] = img_array[y,x + 7],img_array[y,x + 2]


    # Fourth layer of encryption: Combine private and public keys for further modification :
    for y in range(height) :
        for x in range(0,int(width - 1), 2) :
            r,g,b = img_array[y,x]
            r = (r * private_key * public_key) % 256
            g = (g * private_key * public_key) % 256
            b = (b * private_key * public_key) % 256
            img_array[y, x] = [r, g, b]

        for x in range(0,int(width - 1), 2) :
            r,g,b = img_array[y,x + 1]
            r = (r * private_key + public_key) % 256
            g = (g * private_key + public_key) % 256
            b = (b * private_key + public_key) % 256
            img_array[y,x + 1] = [r, g, b]


    # Convert the NumPy array back to an image
    img_modified = Image.fromarray(img_array,"RGB")

    # display and save the modified image
    img_modified.show()
    img_modified.save(output_path)


def decrypt_img(img_path) :
    private_key = int(input("enter your private key : "))
    public_key = int(input("enter your public key : "))

    img1 = Image.open(img_path)      # Open the image using PIL


    # Convert the image to a NumPy array (3D array: height x width x color channels)
    img_array = np.array(img1)

    height, width, channels = img_array.shape
        
    # Reverse of the fourth layer of encryption: Combine private and public keys for further modification :
    for y in range(height) :
        for x in range(0,int(width - 1), 2) :
            r,g,b = img_array[y,x]
            r = (r  * pow(private_key * public_key, -1, 256)) % 256 
            g = (g  * pow(private_key * public_key, -1, 256)) % 256
            b = (b  * pow(private_key * public_key, -1, 256)) % 256
            img_array[y, x] = [r, g, b]

        for x in range(0,int(width - 1), 2) :
            r,g,b = img_array[y,x + 1]
            r = (r - public_key) * pow(private_key, -1, 256)  % 256
            g = (g - public_key) * pow(private_key, -1, 256)  % 256
            b = (b - public_key) * pow(private_key, -1, 256)  % 256
            img_array[y,x + 1] = [r, g, b]


    #  Reverse of the third layer of encryption: Swap pixels in groups of 10 :
    for y in range(height) :
        for x in range(0,int(width - 10), 10) :
            img_array[y,x],img_array[y,x + 8] = img_array[y,x + 8],img_array[y,x]
            img_array[y,x + 9],img_array[y,x + 5] = img_array[y,x + 5],img_array[y,x + 9]
            img_array[y,x + 2],img_array[y,x + 7] = img_array[y,x + 7],img_array[y,x + 2]



    # Reverse of the second layer of encryption: Apply different operations to every third pixel using the private or public key :
    for y in range(height) :
        for x in range(0,int(width - 1), 3) :
            r,g,b = img_array[y,x]
            r = r * pow(private_key, -1, 256) % 256
            g = g * pow(private_key, -1, 256) % 256
            b = b * pow(private_key, -1, 256) % 256
            img_array[y, x] = [r, g, b]
        
        for x in range(0,int(width - 1), 3) :
            r,g,b = img_array[y,x + 1]
            r = (r * pow(public_key, -1 ,256)) % 256
            g = (g + public_key) % 256
            b = (b + public_key) % 256
            img_array[y, x + 1] = [r, g, b]


    # Reverse of the first layer of encryption: Adjust color values using the private key :
    for y in range(height) :
        for x in range(width) :
            r,g,b = img_array[y,x]
            r = (r - private_key + 100) % 256
            g = (g - private_key) % 256
            b = (b - private_key - 150) % 256
            img_array[y, x] = [r, g, b]


    # Convert the NumPy array back to an image
    img_modified = Image.fromarray(img_array,"RGB")

    # display ans save modified image 
    img_modified.show()
    img_modified.save(output_path)



print('''
Welcome to Prodigy, Prodigy is a simple image encryption and decryption tool. Feel free to try it.
 ''')
user_choice = int(input("If you want to encrypt the image insert 1, inseert 2 for decryption : "))

print(r'''
Make sure to remove any quotation marks " or ' from the path before you enter it to avoid problems.

For example : C:\users\lenovo\desktop\test.png"
''')

img_path = input("insert your image's path : ")
output_path = input("insert the path where you want to save the encrypted or decrypted image : ")
if user_choice == 1 :
    encrypt_img(img_path)
elif user_choice == 2 :
    decrypt_img(img_path)
else :
    print("error")
