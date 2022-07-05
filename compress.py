import sys
import json
from typing import List

import data

def get_words(file: str):
    with open(file, 'r') as f:
        words = json.load(f)['words']

    return words


def compress(words: List[str], *, file: str):
    stats = data.get_data(words)

    save = []
    while words:

        word = words[0]
        grams = data.get_trigrams(word)
    
        remaining = [stats['trigrams'][gram] - count for gram, count in grams.items()]

        if (
            stats['boundary']['end'][word[-1]] > 1 and
            stats['boundary']['start'][word[0]] > 1 and
            min(remaining) > 0
        ):
            words.remove(word)
            for gram, count in grams.items():
                stats['trigrams'][gram] -= count

            stats['boundary']['end'][word[-1]] -= 1
            stats['boundary']['start'][word[0]] -= 1
            
            sys.stdout.write(f'{file}: {len(words) + len(save)} words remaining. Removed [{word}] {"":<20}\r')
            sys.stdout.flush()
        else:
            words.remove(word)
            save.append(word)

    print()
    return save


def main():

    files = [
        'english', 
        'english_1k', 
        'english_5k',
        'english_10k', 
        'english_25k', 
        'english_450k',
    ]

    for file in files:
        words = get_words(f'languages/{file}.json')
        saved = compress(words, file=file)

        with open(f'compressed/{file}-pressed.txt', 'w') as f:
            text = ' '.join(saved)
            f.write(text)


if __name__ == '__main__':
    main()