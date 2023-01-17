#FOCP TASK 4
import sys

if len(sys.argv) < 2:
    print("Error: Missing command-line argument.")
    sys.exit(1)

characters = ["\n", " ", ",", ".",";", "(", ")", '"']
def decrypt(text, key):
    decrypted_text = ""
    for c in text:
        if c.isupper():
            decrypted_text +=  chr((ord(c) + key-65) % 26 + 65)
        elif c.islower():
             decrypted_text += chr((ord(c) + key - 97) % 26 + 97)
        elif c in characters:
            decrypted_text += c
    return decrypted_text


def main(files):
    validate= "that" or "the"
    try:
        possibility = 1
        for r in range(1,27):
            plaintext = decrypt(files,r )
            
            if validate in plaintext:
               print("\nPossibility {} Text: {}".format(possibility,  plaintext))
               possibility+=1
            else:
                pass

    except IOError:
        print(f"Error:Cannot open {sys.argv[1]}. Sorry about that.")

with open(sys.argv[1], 'r') as file:
    ciphertext = file.read()
    main(ciphertext)