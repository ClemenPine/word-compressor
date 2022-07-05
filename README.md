# Word Compression
One of the most popular tests used to practice typing is a random sequence of common words. However, these word lists generally contain a lot of repetitition. As a consequence, you'll inevitably practice certain words more often than necessary and other words not often enough.

This tool determines which words in a given list are redundant for practice and discards them, while keeping all others. It does this by calculating the set of trigrams that would comprise a test and then minimizing the list such that the set remains the same size.

### Results
Here are some wordlists from the popular typing website [Monkeytype](https://monkeytype.com) and their word counts before and after compression:
- [eng200](./compressed/english-pressed.txt): 200 -> 174 words
- [eng1k](./compressed/english_1k-pressed.txt): 997 -> 604 words
- [eng5k](./compressed/english_5k-pressed.txt): 4958 -> 1264 words
- [eng10k](./compressed/english_10k-pressed.txt): 9952 -> 1632 words
- [eng25k](./compressed/english_25k-pressed.txt): 24214 -> 2883 words
- [eng450k](./compressed/english_450k-pressed.txt): 451518 -> 7623 words
