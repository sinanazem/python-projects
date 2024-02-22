import random

from utils import generate_word_frequency, print_succes, print_warning, print_not_valid


def run_wordle():
    # Read Words
    words = generate_word_frequency()
    word = random.choice(words)


    num_try = 5

    while True:
        guess = input('Please Enter your words:')

        if guess == 'q':
            break

        num_try -= 1
        if num_try == 0:
            break

        if len(guess) != 5:
            print('your word length must be 5 length! please try again!!!')
            continue

        for w, g in zip(word, guess):
            if w == g:
                print_succes(g, end='')

            elif g in word:
                print_warning(g, end='')

            else:
                print_not_valid(g,  end='\n')
        print()
        if word == guess:
            print('Congratulation!')
            break

if __name__ == "__main__":
    run_wordle()