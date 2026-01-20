def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()_+-={}[]|:;'<>,.?/~`😀😎😂"

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

text = input("Enter your text: ")

while True:
    try:
        shift = int(input("Enter the shift number (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Shift must be between 1 and 25. Please try again.")
    except ValueError:
        print("Please enter a valid integer.")

while True:
    action = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if action in ['e', 'd']:
        break
    else:
        print("Please enter 'e' for encrypt or 'd' for decrypt.")

if action == 'e':
    result = encrypt(text, shift)
else:
    result = decrypt(text, shift)

print("\nResult:", result)
input()
