def decrypt(encrypted_text):
    key = 14
    text_array = list(encrypted_text)
    # A 65
    # Z 90
    # a 97
    # z 122
    # diff 25
    count = 0
    result = ""
    for i in range(len(text_array)):
        letter = text_array[i]
        if (letter.isupper()):
            text_array[i] = chr((ord(letter) + key - 65) % 26 + 65)
        elif (letter.islower()):
            text_array[i] = chr((ord(letter) + key - 97) % 26 + 97)

    return "".join(text_array)


encrypted_text = input()
decrypted_text = decrypt(encrypted_text)

print(decrypted_text)