import random
from typing import List, Tuple
from termcolor import colored, cprint


def read_file(filepath: str) -> List[Tuple]:
    # read data
    with open(filepath) as f:
        data = f.read()

        # split, make list of tuple, and remove None
        data = [tuple(item.split(',')) for item in data.split('\n')[1:] if bool(item) == True]

        # change data type to int for frequency
        data = [(tup[0], int(tup[1])) for tup in data]

        #sort frequency as decending
        data = sorted(data, key=lambda x: x[1], reverse=True)
    return data


def generate_word_frequency(word_len: int=5, limit: int=1000)-> List[Tuple]:
    # Read Data
    data = read_file('src/data/unigram_freq.csv')

    # Filter Words Length
    data = list(filter(lambda word_freq: len(word_freq[0]) == word_len , data))

    # Limit Data
    data = data[:limit]
    words = [word_freq[0] for word_freq in data]
    return words

def print_succes(text, end=''):
    print(colored(text, "green", attrs=["reverse"]), end='')

def print_warning(text, end=''):
    print(colored(text, "yellow", attrs=["reverse"]), end='')

def print_erorr(text, end=''):
    print(colored(text, "red", attrs=["reverse"]), end='')

def print_not_valid(text, end=''):
    print(colored(text, "grey", attrs=["reverse"]), end='')

