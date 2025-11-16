import time

chars = list("1234567890qwertyuiopmasdfghjklzxcvbnQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()[];',/. ")

def premium_print(text: str):
    temp_text = ["" for _ in range(len(text))]
    searching_letter_index = 0
    for letter in text:
        temp_letter_index = 0
        temp_letter = chars[temp_letter_index]
        while temp_letter != letter:
            temp_letter_index += 1
            temp_letter = chars[temp_letter_index]
            temp_text[searching_letter_index] = temp_letter
            print("".join(temp_text))
            time.sleep(0.02)
        searching_letter_index += 1


premium_print("Hello world!")