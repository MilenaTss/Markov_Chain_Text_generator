from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import random


def is_end_of_sentence(x):
    return x.endswith('.') or x.endswith('?') or x.endswith('!')


def create_data():
    print("Input name of file with data")
    name_of_file = input()
    file = open(name_of_file, 'r', encoding='utf-8')
    text = file.read()
    file.close()
    words = WhitespaceTokenizer().tokenize(text)
    bigrams = [words[i] + ' ' + words[i + 1] for i in range(len(words) - 1)]

    # key is word, value is dict where key is word and value is num of such bigrams
    dict_with_bigrams = {}
    list_of_bigrams = Counter(bigrams).most_common()

    for bigram in list_of_bigrams:
        current_ = bigram[0].split()
        dict_with_bigrams.setdefault(current_[0], {})
        dict_with_bigrams[current_[0]][current_[1]] = bigram[1]
    return words, dict_with_bigrams


if __name__ == '__main__':
    words, dict_with_bigrams = create_data()
    print("Input number of sentences")

    n = int(input())
    for i in range(n):
        current_word = None
        for j in range(80):
            # first word
            while not current_word:
                current_word = random.choice(words)
                if not current_word[0].isupper() or is_end_of_sentence(current_word):
                    current_word = None
            else:
                if j == 0:
                    print(current_word, end=" ")
            tails = [i for i in dict_with_bigrams[current_word].keys()]
            nums = [i for i in dict_with_bigrams[current_word].values()]
            current_word = random.choices(tails, nums)[0]
            print(current_word, end=" ")
            if j >= 4 and (is_end_of_sentence(current_word)):
                break
        print()
