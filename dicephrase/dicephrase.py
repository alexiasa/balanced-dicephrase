import requests
import random


def generate_keyboard():
    keyboard = {
        "1": (-5, 2),
        "2": (-4, 2),
        "3": (-3, 2),
        "4": (-2, 2),
        "5": (-1, 2),
        "6": (1, 2),
        "7": (2, 2),
        "8": (3, 2),
        "9": (4, 2),
        "0": (5, 2),
        "q": (-5, 1),
        "w": (-4, 1),
        "e": (-3, 1),
        "r": (-2, 1),
        "t": (-1, 1),
        "y": (1, 1),
        "u": (2, 1),
        "i": (3, 1),
        "o": (4, 1),
        "p": (5, 1),
        "a": (-5, 0),
        "s": (-4, 0),
        "d": (-3, 0),
        "f": (-2, 0),
        "g": (-1, 0),
        "h": (1, 0),
        "j": (2, 0),
        "k": (3, 0),
        "l": (4, 0),
        "z": (-5, -1),
        "x": (-4, -1),
        "c": (-3, -1),
        "v": (-2, -1),
        "b": (-1, -1),
        "n": (1, -1),
        "m": (2, -1),
        " ": (0, 0)
    }

    return keyboard


def get_word_list(list_name):
    if list_name == 'eff':
        word_list = requests.get('https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt')
        return word_list
    else:
        word_list = '/usr/share/dict/web2'  # local word list
        return word_list


def get_random_words(text, num_words=5):
    generated_words = []
    while len(generated_words) < num_words:
        choice = random.choice(text)
        generated_words.append(choice)
    return " ".join(generated_words)


def filter_length(input, min_length, max_length):
    return list([x for x in input if min_length <= len(x) <= max_length])


def get_scores(words):
    scores = []
    for word in words:
        scores.append(get_word_scores(word))
    return scores


def get_word_scores(words):
    scores = []
    for word in words:
        for letter in word:
            scores.append(generate_keyboard()[letter])
    return scores


def calc_offset(scores):
    return sum(scores)


if __name__ == '__main__':

    dictionary = str(get_word_list('none'))
    text = open(dictionary, 'r').read().lower().splitlines()
    text = filter_length(text, 5, 7)

    for i in range(1, 5):
        all_scores = []
        for x in range(1, 1000):
            word = get_random_words(text, 1)
            scores = get_scores(word)
            score = calc_offset(scores)
            all_scores.append((word, score))

        sorted_scores = sorted(all_scores, key=lambda x: abs(x[1]), reverse=True)

        balanced = sorted_scores[-4:]

        werds = []
        for bal in balanced:
            werds.append(bal[0])

        print(" ".join(werds))
