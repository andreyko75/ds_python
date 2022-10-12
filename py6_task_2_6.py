# Модифицируем предыдущую задачу.
# Теперь необходимо написать функцию get_most_frequent_word, которое возвращает самое часто встречающееся слово в тексте.
import re
from functools import reduce

text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."


def get_most_frequent_word(text):
    text_temp = list(sorted((re.sub(r'[^\w\s]', '', text.lower())).split(' ')))
    print(text_temp)
    word_s = reduce(lambda x, y: x if (text_temp.count(x) > text_temp.count(y)) else y, text_temp)
    return word_s


print(get_most_frequent_word(text_example))
