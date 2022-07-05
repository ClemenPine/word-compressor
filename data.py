from collections import Counter
from typing import List


def get_trigrams(word: str):
    word = f' {word} '
    grams = [''.join(x) for x in zip(word, word[1:], word[2:])]
    return Counter(grams)


def get_data(words: List[str]):
    
    data = {
        'trigrams': {},
        'boundary': {},
    }

    counts = {
        'start': {},
        'end': {},
    }

    for word in words:

        padded_word = ' ' + word + ' '
        for i in range(len(padded_word) - 2):
            seq = padded_word[i:i+3]
            if not seq in data['trigrams']:
                data['trigrams'][seq] = 1
            else:
                data['trigrams'][seq] += 1

        if not word[0] in counts['start']:
            counts['start'][word[0]] = 1
        else:
            counts['start'][word[0]] += 1

        if not word[-1] in counts['end']:
            counts['end'][word[-1]] = 1
        else:
            counts['end'][word[-1]] += 1

    data['boundary'] = counts

    return data