# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word multiplied by the length of the word, plus 50
    points if all n letters are used on the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0

    for char in word:
        score += SCRABBLE_LETTER_VALUES[char]

    score *= len(word)

    if len(word) == n:
        score += 50

    return score


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line


def get_displayable_hand(hand):
    """
    Returns string of letters in hand.
    String will be similar to output of 'display_hand' function

    hand: dictionary (string -> int)
    """

    output = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
            output += letter + ' '

    return output[:-1]

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    hand_remaining = {}
    for key in hand.keys():
        hand_remaining[key] = hand[key]

    for char in word:
        freq = 0
        freq = hand_remaining[char] - 1

        if freq == 0:
            del hand_remaining[char]
        else:
            hand_remaining[char] = freq

    return hand_remaining


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    if not word in word_list:
        return False

    word_dict = get_frequency_dict(word)
    hand_keys = hand.keys()
    for key in word_dict.keys():
        if key not in hand_keys or word_dict[key] > hand[key]:
            return False

    return True



def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen


def get_word(hand, word_list):
    """
    Repeatedly (recursively) prompts player for a word to play
    until a valid word or a "." is returned.

    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    word = raw_input(
        'Enter a word, or a "." to indicate you are finished: ')

    word = word.lower()

    if word == "." or is_valid_word(word, hand, word_list):
        return word
    else:
        print "Invalid word. Please try again."
        return get_word(hand, word_list)


#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings

    """
    total_score = 0
    while calculate_handlen(hand) > 0:
        print
        print 'Current hand: {}'.format(get_displayable_hand(hand))
        word = get_word(hand, word_list)

        if word == '.':
            break
        else:
            word_score = get_word_score(word, calculate_handlen(hand))
            total_score += word_score
            print '"{0}" scored {1:d} points. Total: {2:d} points'.format(
                word, word_score, total_score)
            hand = update_hand(hand, word)

    print
    print 'Total score: {0:d} points.'.format(total_score)


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
#
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    hand = {}

    while True:
        user_action = ''
        print
        print
        print 'Main Menu:'
        print '----------'
        print 'n - deals a new, random hand'

        if calculate_handlen(hand) > 0:
            print 'r - replays the previous hand'

        print 'e - exits'
        print
        user_action = raw_input("Your choice: ")

        if user_action == 'e':
            print "Goodbye!"
            break

        if user_action == 'n':
            hand = deal_hand(HAND_SIZE)

        if user_action == 'r' or user_action == 'n':
            play_hand(hand, word_list)


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
