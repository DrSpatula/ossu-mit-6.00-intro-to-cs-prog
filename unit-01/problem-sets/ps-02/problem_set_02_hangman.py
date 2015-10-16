# 6.00 Problem Set 3
#
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


def update_available_letters(guess, remaining_letters):
    """
    guess (string, single character): guessed letter to remove from remaining
                                      unguessed letters

    remaining_letters (string): current string of unguessed letters

    Returns the string of unguessed letters with the latest guess removed
    """
    idx = remaining_letters.find(guess)

    if idx != -1:
        remaining_letters = remaining_letters[:idx] + '_' +\
            remaining_letters[(idx + 1):]

    return remaining_letters


def find_all(guess, word):
    """
    guess (string, single character): guessed letter to find in word
    word (string): word to find instances of guess in

    Returns tuple containing indexes of occurances of guess in word
    """
    idx = 0
    num_occurances = word.count(guess)
    occurances = ()

    while len(occurances) < num_occurances:
        idx = word.find(guess, idx)
        if idx != -1:
            occurances = occurances + (idx, )
            idx += 1

    return occurances


def update_blanks(guess, word, blanks):
    """
    guess (string, single character): guessed letter
    word (string): current word being guessed
    blanks (string): display of progress towards guessing the word

    Returns blanks with guessed letter replacing the blanks at the
    corresponding places they occur in word
    """
    occurances = find_all(guess, word)

    for idx in occurances:
        blanks = blanks[:idx] + guess + blanks[(idx + 1):]

    return blanks


def valid_guess(guess):
    """
    guess (string): the guess to validate

    Returns true if guess is a string containing a single, lowercase letter
    """
    return len(guess) == 1 and guess in string.lowercase

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program

wordlist = load_words()
word = choose_word(wordlist)
word_progress = '_' * len(word)
letters_available = string.lowercase
guesses_left = 8
guess = ''

print '\nWelcome to hangman!'
print 'I am thinking of a word that is {0:d} letters long.'.format(len(word))

while guesses_left > 0 and '_' in word_progress:
    print '------------'
    print 'You have {0:d} guesses left'.format(guesses_left)
    print 'Available letters: {0}'.format(letters_available)

    while not valid_guess(guess):
        guess = raw_input('Please guess a single letter: ').lower()

    if guess in word:
        word_progress = update_blanks(guess, word, word_progress)
        print 'Good guess! {0}'.format(word_progress)
    else:
        guesses_left -= 1
        print 'Nope. {0}'.format(word_progress)

    letters_available = update_available_letters(guess, letters_available)
    guess = ''

if '_' not in word_progress:
    print 'Congratulations!  You have won!'
else:
    print 'You ran out of guesses. The word was "{0}"'.format(word)
