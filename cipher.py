# add your code here
def take_input():
    sentence_to_encrypt = input("Please enter the sentence you would like to encrypt:").lower()
    return sentence_to_encrypt
    pass


def cipher(word):
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    encrypted_phrase = " "
    shift = 5
    for char in word:
        if char in alphabet:
            index = alphabet.find(char)
            if index >= 21:
                char = alphabet[index - 21]
                encrypted_phrase += char
            elif index <= 21:
                char = alphabet[index + shift]
                encrypted_phrase += char
        else:
            encrypted_phrase += char
    return encrypted_phrase

def main():
    word = take_input()
    cipher(word)
    print("The encrypted phrase is:"," ", cipher(word))
main()
