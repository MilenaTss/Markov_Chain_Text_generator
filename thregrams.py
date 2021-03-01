from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import random

name_of_file = input()
file = open(name_of_file, 'r', encoding='utf-8')
text = file.read()
file.close()
words = WhitespaceTokenizer().tokenize(text)
bigram = [words[i] + ' ' + words[i + 1] for i in range(len(words) - 1)]
threegram = [words[i] + ' ' + words[i + 1] + ' ' + words[i + 2] for i in range(len(words) - 2)]

_dict = {}
_list = Counter(threegram).most_common()
for i in _list:
    word = i[0].split()
    bi = word[0] + ' ' + word[1]
    _dict.setdefault(bi, {})
    _dict[bi][word[2]] = i[1]

for i in range(10):
    word = None
    for j in range(80):
        while not word:
            word = random.choice(bigram)
            x = word.split()[0]
            if not word[0].isupper() or x.endswith('.') or x.endswith('?') or x.endswith('!'):
                word = None
        else:
            if j == 0:
                print(word, end=" ")
        prev = word.split()[1]
        tails = [i for i in _dict[word].keys()]
        nums = [i for i in _dict[word].values()]
        word = random.choices(tails, nums)[0]
        if prev.endswith('.') or prev.endswith('?') or prev.endswith('!'):
            while not word[0].isupper():
                word = random.choices(tails, nums)[0]
        print(word, end=" ")
        if j >= 2 and (word.endswith('.') or word.endswith('?') or word.endswith('!')):
            break
        word = prev + ' ' + word
    print()
