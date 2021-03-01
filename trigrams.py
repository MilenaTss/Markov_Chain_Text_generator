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
    trigrams = [words[i] + ' ' + words[i + 1] + ' ' + words[i + 2] for i in range(len(words) - 2)]

    # key is bigram, value is dict where key is third word and value is num of such trigrams
    dict_with_trigrams = {}
    list_of_trigrams = Counter(trigrams).most_common()

    for i in list_of_trigrams:
        current_word = i[0].split()
        bi = current_word[0] + ' ' + current_word[1]
        dict_with_trigrams.setdefault(bi, {})
        dict_with_trigrams[bi][current_word[2]] = i[1]
    return bigrams, dict_with_trigrams


if __name__ == '__main__':
    bigrams, dict_with_trigrams = create_data()
    print("Input number of sentences")
    
    n = int(input())
    for i in range(n):
        current_word = None
        for j in range(80):
            # first word
            while not current_word:
                current_word = random.choice(bigrams)
                first = current_word.split()[0]
                if not current_word[0].isupper() or is_end_of_sentence(first):
                    current_word = None
            else:
                if j == 0:
                    print(current_word, end=" ")

            previous = current_word.split()[1]
            tails = [i for i in dict_with_trigrams[current_word].keys()]
            nums = [i for i in dict_with_trigrams[current_word].values()]
            current_word = random.choices(tails, nums)[0]
            if is_end_of_sentence(previous):
                while not current_word[0].isupper():
                    current_word = random.choices(tails, nums)[0]
            print(current_word, end=" ")
            if j >= 2 and (is_end_of_sentence(current_word)):
                break
            current_word = previous + ' ' + current_word
        print()
