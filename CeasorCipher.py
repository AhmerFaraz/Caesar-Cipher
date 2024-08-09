logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
# List of alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(message, ciphert):
    message_list = []

    for letters in message:
        message_list.append(letters)

    shifted_list = []

    for letters in message_list:
        if letters in alphabet:
            index_value = alphabet.index(letters)
            shifted_letters = alphabet[index_value + ciphert]
            shifted_list.append(shifted_letters)
        else:
            shifted_list.append(letters)

    shifted_message = ""
    for char in shifted_list:
        shifted_message += char

    print(f"Encrypted message is: \n{shifted_message}")


def decrypt(ciphertext, ciphert):
    ciphertext_list = []

    for letters in ciphertext:
        ciphertext_list.append(letters)

    original_list = []

    for letters in ciphertext_list:
        if letters in alphabet:
            index_value = alphabet.index(letters)
            shifted_letters = alphabet[index_value - ciphert]
            original_list.append(shifted_letters)
        else:
            original_list.append(letters)

    original_message = ""
    for char in original_list:
        original_message += char

    print(f"Decrypted message is: \n{original_message}")


print(logo)
end_program = False
while not end_program:
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt: \n").lower()
    if direction == "encode":
        text = input("Type your message: \n").lower()
        shift_no = int(input("Type the shift number: \n"))
        shift_no = shift_no % 26
        encrypt(text, shift_no)
    elif direction == "decode":
        text = input("Type your message: \n").lower()
        back_shift = int(input("Type the shift number: \n"))
        back_shift = back_shift % 26
        decrypt(text, back_shift)
    else:
        print("Please Enter valid choice!!")

    end_instruction = input("Type 'yes' if you want to continue or type 'no' to end the program. \n").lower()
    if end_instruction == "yes":
        end_program = False
    elif end_instruction == "no":
        end_program = True
    else:
        print("Enter valid choice")
        end_program = False
