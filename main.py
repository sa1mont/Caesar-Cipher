word = input('Напишите сообщение, которое вам нужно расшифровать или зашифровать.')
is_decryption = int(input('Нужно расшифровать (1) или зашифровать (2)? Напишите соответствующую цифру'))
decryp_language = int(input('Какой язык используется? Русский (1) или английский (2)? Напишите соответствующую цифру'))
step = int(input('Напишите шаг сдвига'))

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
chars = ',.?/!\\`-_ 0123456789'

def decription(word):
    b = ''
    for i in range(len(word)):
        a = 0
        if decryp_language == 1 and word[i] in rus_lower_alphabet:
            a = rus_lower_alphabet[word[i]]
            b += (rus_lower_alphabet[a + step]) % 32
        elif decryp_language == 1 and word[i] in rus_upper_alphabet:
            a = rus_upper_alphabet[word[i]]
            b += (rus_upper_alphabet[a + step]) % 32
        elif decryp_language == 2 and word[i] in eng_lower_alphabet:
            a = eng_lower_alphabet[word[i]]
            b += (eng_lower_alphabet[a + step]) % 32
        elif decryp_language == 2 and word[i] in eng_upper_alphabet:
            a = eng_upper_alphabet[word[i]]
            b += (eng_upper_alphabet[a + step]) % 32
        elif word[i] in chars:
            b += word[i]
    return b

if is_decryption == 1:
    print(decription(word))