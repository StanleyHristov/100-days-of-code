
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

messege = input("What you want to do 'encrypt' or 'decrypt'? ")
text = input("What is the message you want to transcript").lower()
shift = int(input("What is the shift number?"))

def encrypt(text, shift):
    new_list = []
    new_text = list(text)
    for letter in new_text:
         for i in range(len(alphabet)):
             if letter == alphabet[i]:
                 if shift+i<len(alphabet):
                    new_list.append(alphabet[i+shift])
                 else:
                    new_list.append(alphabet[i+shift-len(alphabet)])
    print("".join(new_list))

def decrypt(text, shift):
    new_list = []
    new_text = list(text)
    for letter in new_text:
         for i in range(len(alphabet)):
             if letter == alphabet[i]:
                 if shift<0:
                    new_list.append(alphabet[i+shift])
                 else:
                    new_list.append(alphabet[i-shift])
    print("".join(new_list))


if messege == 'encrypt':
    encrypt(text , shift)
elif messege == 'decrypt':
    decrypt(text,shift)
else:
    print("Error run the program again and chouse from the options")