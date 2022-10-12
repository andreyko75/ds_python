# Напишите функцию get_unique_words(), которая избавляется от знаков препинаний
# и пробелов в тексте и возвращает упорядоченный список
# (слова расположены по алфавиту) из уникальных (неповторяющихся) слов.

# Можно использовать готовый список со знаками препинания:
import re
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
# Текст, который можно использовать в качестве примера:
text_example = "A beginning is the time for taking the most delicate " \
               "care that the balances are correct. This every sister of the Bene Gesserit knows." \
               " To begin your study of the life of Muad'Dib, then take care that you first place him " \
               "in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most " \
               "special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by " \
               "the fact that he was born on Caladan and lived his first fifteen years there. Arrakis," \
               " the planet known as Dune, is forever his place."

def get_unique_words(text):
    return sorted(list(set((re.sub(r'[^\w\s]', '', text.lower())).split(' '))))


print(get_unique_words(text_example))


